import argparse
import logging
import os
import time

import cv2
import fitz
import numpy as np
import torch
import unimernet.tasks as tasks
import yaml
from PIL import Image
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from ultralytics import YOLO
from unimernet.common.config import Config
from unimernet.processors import load_processor

from magic_doc.model.sub_modules.layoutlmv3.model_init import Layoutlmv3_Predictor
from magic_doc.model.sub_modules.post_process import (
    get_croped_image,
    latex_rm_whitespace,
)
from magic_doc.model.parallel_ocr import ParallelOCR
from magic_doc.model.seq_ocr import SeqOCR
from magic_doc.model.parallel_layout import ParallelLayout
from magic_doc.model.seq_layout import SeqLayout

import paddle 

from magic_doc.utils.yaml_load import patch_yaml_load_with_env
from magic_doc.utils import get_repo_directory

logging.disable(logging.WARNING)


class MathDataset(Dataset):
    def __init__(self, image_paths, transform=None):
        self.image_paths = image_paths
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        # if not pil image, then convert to pil image
        if isinstance(self.image_paths[idx], str):
            raw_image = Image.open(self.image_paths[idx])
        else:
            raw_image = self.image_paths[idx]
        if self.transform:
            image = self.transform(raw_image)
        return image


class DocAnalysis(object):
    """
    Description:
      class definition of DocAnalysis module:
    """

    def __init__(
        self, configs="magic_doc/resources/model/model_configs.yaml", **kwargs
    ):
        """
        Description:
          initialize the class instance

        Parameters:
          configs: path to config that contains model weights.
          apply_layout: do layout analysis or not, must be True (defaults to be True).
          apply_formula: do formulat detection and recognition or not, defaults to be False.
          apply_ocr: do ocr(text detection and recognition) or not, defaults to be False.

        """
        self.configs = patch_yaml_load_with_env(configs, "model", yaml.FullLoader)  # load config and patch with env var !
        self.apply_layout = kwargs.get("apply_layout", self.configs["models"]["layout"])
        self.apply_formula = kwargs.get(
            "apply_formula", self.configs["models"]["formula"]
        )
        self.apply_ocr = kwargs.get("apply_ocr", self.configs["models"]["ocr"])
        logging.info(
            "DocAnalysis init, this may take some times. apply_layout: {}, apply_formula: {}, apply_ocr: {}".format(
                self.apply_layout, self.apply_formula, self.apply_ocr
            )
        )
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logging.info("using device: {}".format(self.device))
        assert self.apply_layout, "DocAnalysis must contain layout model."

        if torch.cuda.device_count() > 1:
            self.layout_model = ParallelLayout(self.configs["weights"]["layout"])
        else:
            self.layout_model = SeqLayout(self.configs["weights"]["layout"])

        if self.apply_formula:
            self.mfd_model = YOLO(self.configs["weights"]["mfd"])
            args = argparse.Namespace(
                cfg_path=os.path.join(get_repo_directory(), "resources/model/UniMERNet/demo_old.yaml"),
                options=None,
            )
            cfg = Config(args)
            cfg.config.model.pretrained = os.path.join(
                self.configs["weights"]["mfr"], "pytorch_model.bin"
            )
            cfg.config.model.model_config.model_name = self.configs["weights"]["mfr"]
            cfg.config.model.tokenizer_config.path = self.configs["weights"]["mfr"]
            task = tasks.setup_task(cfg)
            model = task.build_model(cfg)
            self.mfr_model = model.to(self.device)
            mfr_vis_processor = load_processor(
                "formula_image_eval",
                cfg.config.datasets.formula_rec_eval.vis_processor.eval,
            )
            self.mfr_transform = transforms.Compose(
                [
                    mfr_vis_processor,
                ]
            )
        if self.apply_ocr:
            if paddle.device.cuda.device_count() > 1:
                self.ocr_model = ParallelOCR()
            else:
                self.ocr_model = SeqOCR(use_gpu=True)

        logging.info("DocAnalysis init done!")

    def __call__(self, image_list):
        """
        Description:
          do document analysis on input images

        Parameters:
          image_list: list of image array, [np.array, ...]

        Return:
          result: doc analysis result
        """
        doc_layout_result = []
        latex_filling_list = []
        mf_image_list = []

        layout_inference_reqs = [] 

        for idx, image in enumerate(image_list):
            layout_inference_reqs.append((idx, image)) # 

        layout_inference_results = self.layout_model(layout_inference_reqs)

        for idx, layout_res in layout_inference_results:
            image = image_list[idx]
            img_H, img_W = image.shape[0], image.shape[1]

            if self.apply_formula:
                mfd_res = self.mfd_model.predict(
                    image, imgsz=1888, conf=0.25, iou=0.45, verbose=False
                )[0]
                for xyxy, conf, cla in zip(
                    mfd_res.boxes.xyxy.cpu(),
                    mfd_res.boxes.conf.cpu(),
                    mfd_res.boxes.cls.cpu(),
                ):
                    xmin, ymin, xmax, ymax = [int(p.item()) for p in xyxy]
                    new_item = {
                        "category_id": 13 + int(cla.item()),
                        "poly": [xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax],
                        "score": round(float(conf.item()), 2),
                        "latex": "",
                    }
                    layout_res["layout_dets"].append(new_item)
                    latex_filling_list.append(new_item)
                    bbox_img = get_croped_image(
                        Image.fromarray(image), [xmin, ymin, xmax, ymax]
                    )
                    mf_image_list.append(bbox_img)

            layout_res["page_info"] = dict(page_no=idx, height=img_H, width=img_W)
            doc_layout_result.append(layout_res)
        
        if self.apply_formula:
            a = time.time()
            dataset = MathDataset(mf_image_list, transform=self.mfr_transform)
            dataloader = DataLoader(dataset, batch_size=128, num_workers=32)
            mfr_res = []
            for imgs in dataloader:
                imgs = imgs.to(self.device)
                output = self.mfr_model.generate({"image": imgs})
                mfr_res.extend(output["pred_str"])
            for res, latex in zip(latex_filling_list, mfr_res):
                res["latex"] = latex_rm_whitespace(latex)
            b = time.time()
            logging.info(
                "formula nums: {}, mfr time: {}".format(
                    len(mf_image_list), round(b - a, 2)
                )
            )

        if self.apply_ocr:
            ocr_det_reqs = []

            a = time.time()
            for idx, image in enumerate(image_list):
                pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
                single_page_res = doc_layout_result[idx]["layout_dets"]
                single_page_mfdetrec_res = []
                if self.apply_formula:
                    for res in single_page_res:
                        if int(res["category_id"]) in [13, 14]:
                            xmin, ymin = int(res["poly"][0]), int(res["poly"][1])
                            xmax, ymax = int(res["poly"][4]), int(res["poly"][5])
                            single_page_mfdetrec_res.append(
                                {
                                    "bbox": [xmin, ymin, xmax, ymax],
                                }
                            )
                for res in single_page_res:
                    if int(res["category_id"]) in [
                        0,
                        1,
                        2,
                        4,
                        6,
                        7,
                    ]:
                        xmin, ymin = int(res["poly"][0]), int(res["poly"][1])
                        xmax, ymax = int(res["poly"][4]), int(res["poly"][5])
                        crop_box = [xmin, ymin, xmax, ymax]
                        cropped_img = Image.new("RGB", pil_img.size, "white")
                        cropped_img.paste(pil_img.crop(crop_box), crop_box)
                        cropped_img = cv2.cvtColor(
                            np.asarray(cropped_img), cv2.COLOR_RGB2BGR
                        )
                        ocr_det_reqs.append((idx, cropped_img, single_page_mfdetrec_res))

            for idx, ocr_res in self.ocr_model(ocr_det_reqs):
                if ocr_res:
                    for box_ocr_res in ocr_res:
                        p1, p2, p3, p4 = box_ocr_res[0]
                        text, score = box_ocr_res[1]
                        doc_layout_result[idx]["layout_dets"].append(
                            {
                                "category_id": 15,
                                "poly": p1 + p2 + p3 + p4,
                                "score": round(score, 2),
                                "text": text,
                            }
                        )
            b = time.time()
            logging.info("ocr time: {}".format(round(b - a, 2)))
        return doc_layout_result


def load_images_from_pdf(pdf_data_bytes, dpi=72):
    doc = fitz.open("pdf", pdf_data_bytes)
    images = []

    for i in range(len(doc)):
        page = doc[i]
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        # images.append(image)
        images.append(np.array(image)[:, :, ::-1])
    return images


if __name__ == "__main__":
    doc_proc = DocAnalysis(apply_ocr=True, apply_layout=True, apply_formula=False)
    with open("/opt/data/pdf/20240423/pdf_test2/tc.2013.10.pdf", "rb") as f:
        data = f.read()
        results = doc_proc(load_images_from_pdf(data))
    print(results)

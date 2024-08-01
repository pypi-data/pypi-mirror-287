import os
from typing import Any, List
import numpy as np
import gdown
from deepface.models.Detector import Detector, FacialAreaRegion
from deepface.commons import folder_utils
from deepface.commons import logger as log

logger = log.get_singletonish_logger()

# Model's weights paths
PATH = "/.deepface/weights/yolov8n-face.pt"

# Google Drive URL from repo (https://github.com/derronqi/yolov8-face) ~6MB
WEIGHT_URL = "https://drive.google.com/uc?id=1qcr9DbgsX3ryrz2uU8w4Xm3cOrRywXqb"


class YoloClient(Detector):
    def __init__(self):
        self.model = self.build_model()

    def build_model(self) -> Any:
        """
        Build a yolo detector model
        Returns:
            model (Any)
        """

        # Import the Ultralytics YOLO model
        try:
            from ultralytics import YOLO
        except ModuleNotFoundError as e:
            raise ImportError(
                "Yolo is an optional detector, ensure the library is installed. "
                "Please install using 'pip install ultralytics'"
            ) from e

        weight_path = f"{folder_utils.get_deepface_home()}{PATH}"

        # Download the model's weights if they don't exist
        if not os.path.isfile(weight_path):
            logger.info(f"Downloading Yolo weights from {WEIGHT_URL} to {weight_path}...")
            try:
                gdown.download(WEIGHT_URL, weight_path, quiet=False)
            except Exception as err:
                raise ValueError(
                    f"Exception while downloading Yolo weights from {WEIGHT_URL}."
                    f"You may consider to download it to {weight_path} manually."
                ) from err
            logger.info(f"Yolo model is just downloaded to {os.path.basename(weight_path)}")

        # Return face_detector
        return YOLO(weight_path)

    def detect_faces(self, img: np.ndarray, persist: bool = True) -> List[FacialAreaRegion]:
        """
        Detect and align face with yolo

        Args:
            img (np.ndarray): pre-loaded image as numpy array

        Returns:
            results (List[FacialAreaRegion]): A list of FacialAreaRegion objects
        """
        resp = []

        # Detect faces
        print("persist 1", persist)
        logger.info(f"Persist: {persist}")
        results = self.model.track(img, device='0', persist=persist, verbose=False, show=False, conf=0.25)

        # For each face, extract the bounding box, the landmarks and confidence
        for result in results:

            if result.boxes is None or result.keypoints is None:
                continue

            for idx, box in enumerate(result.boxes):
                # Extract the bounding box and the confidence
                x, y, w, h = box.xywh[0].tolist()
                confidence = box.conf[0].item()
                track_id = 0 if box.id is None else box.id.item()

                # right_eye_conf = result.keypoints.conf[0][0]
                # left_eye_conf = result.keypoints.conf[0][1]
                right_eye = result.keypoints.xy[idx][0].tolist()
                left_eye = result.keypoints.xy[idx][1].tolist()

                # eyes are list of float, need to cast them tuple of int
                left_eye = tuple(int(i) for i in left_eye)
                right_eye = tuple(int(i) for i in right_eye)

                x, y, w, h = int(x - w / 2), int(y - h / 2), int(w), int(h)
                facial_area = FacialAreaRegion(
                    x=x,
                    y=y,
                    w=w,
                    h=h,
                    left_eye=left_eye,
                    right_eye=right_eye,
                    confidence=confidence,
                    track_id=track_id
                )
                resp.append(facial_area)

        return resp

# Made by Isaac Joffe

import cv2
import numpy as np
from .yolov5 import detect as yolo


def run_features(image_name, model_name):
    return yolo.get_data(weights=(model_name + "weights/best.pt"), source=image_name, data=(model_name + "data.yaml"), imgsz=(1280, 1280), project="/tmp/detect/")


def run_segmenter(image_name, model_name):
    return yolo.get_data(weights=(model_name + "weights/best.pt"), source=image_name, data=(model_name + "data.yaml"), imgsz=(192, 192), project="/tmp/detect/")


def main():
    return


if __name__ == "__main__":
    main()

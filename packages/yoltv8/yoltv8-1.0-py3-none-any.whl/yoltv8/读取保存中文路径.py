import cv2
import os
import numpy as  np


def cvimread(path):
    """读取中文路径图片."""
    return cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)


def cvimwrite(path, img):
    """保存中文路径图片."""
    path = os.path.abspath(path)
    cat = os.path.split(path)[0]
    if not os.path.exists(cat):
        os.makedirs(cat)
    c = '.'+path.split('.')[-1]
    cv2.imencode(c, img)[1].tofile(path)
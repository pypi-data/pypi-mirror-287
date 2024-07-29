from ultralytics import YOLO
import cv2
from ultralytics.engine.results import Results
import numpy as np
# Load a model
model = YOLO(r'C:\Users\xuzhe\Desktop\yolo_High\weights\VisDrone.pt')  # pretrained YOLOv8n model

source = r"C:\Users\xuzhe\Desktop\First_task\v8_High_resolution\input\img.png"
# source = r'D:\YOLOv8\video\4.mp4'

# Run inference on the source
results = model(source, save=True, save_txt=True,conf=0.25)  # list of Results objects

# print(results[0].boxes.cls)
# print(results[0].boxes.xywh)
results[0].show()

# images_path = r'C:\Users\xuzhe\Desktop\First_task\v8_High_resolution\input\img.png'
# class_names = [
#     "WBC",
#     "malaria"]
# image = cv2.imread(images_path)
# boxes_list = [[10, 20, 30, 40,1,2], [50, 60, 70, 80,1,2]]
# empty_boxes = np.empty((0, 6))
# boxes_array = np.array(boxes_list)
# a = Results(orig_img=image, path=images_path, names=class_names,boxes=empty_boxes)
#
# print(a.boxes.xywh)
# print(a.boxes.cls)
# print(a.boxes.conf)

'''
source: 输入源，可以是图片路径、视频文件路径或摄像头索引（如 0 表示第一个摄像头）。
show: 布尔值，如果设置为 True，则在屏幕上显示检测结果。
save: 布尔值，如果设置为 True，则将检测结果保存到文件中。
device: 指定运行模型的设备，可以是 'cpu' 或 'cuda'（如果可用）。
classes: 一个整数列表，指定要检测的类别索引。如果设置为 [0]，则检测所有类别。
hide_conf: 布尔值，如果设置为 True，则隐藏置信度较低的检测结果。
hide_labels: 布尔值，如果设置为 True，则隐藏检测框上的类别标签。
augment: 布尔值，如果设置为 True，则对输入图像进行数据增强。
half: 布尔值，如果设置为 True，使用半精度（float16）进行推理，以加快速度。
dnn: 布尔值，如果设置为 True，使用OpenCV的DNN模块进行推理。
visualize: 布尔值或函数，如果设置为 True，则使用默认的可视化函数显示结果；如果提供了函数，则使用该函数进行自定义可视化。
update: 布尔值，如果设置为 True，在每次检测后更新模型的统计信息。
project: 保存模型预测结果的目录路径。
name: 保存的预测结果的文件名前缀。
exist_ok: 布尔值，如果设置为 True，则允许覆盖已存在的文件。
save_txt=True
'''

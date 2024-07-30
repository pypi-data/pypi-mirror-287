import os
import sys
import argparse
from ultralytics import YOLO
import shutil

PROJECT_ROOT = os.path.abspath(os.path.join(os.getcwd(), "."))
sys.path.append(PROJECT_ROOT)
sys.path.append(os.path.join(PROJECT_ROOT, "utils"))
# from utils.slice_images import slice_image
# from utils.convert_coordinates import convert_coordinates
# from utils.draw_pred_on_onr_img import draw_predictions_on_image
import cv2
import time
import numpy as np
from ultralytics.engine.results import Results
import math


class Colors:
    # Ultralytics color palette https://ultralytics.com/
    def __init__(self):
        # hex = matplotlib.colors.TABLEAU_COLORS.values()
        hex = ('FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231', '48F90A', '92CC17', '3DDB86', '1A9334', '00D4BB',
               '2C99A8', '00C2FF', '344593', '6473FF', '0018EC', '8438FF', '520085', 'CB38FF', 'FF95C8', 'FF37C7')
        self.palette = [self.hex2rgb('#' + c) for c in hex]
        self.n = len(self.palette)

    def __call__(self, i, bgr=False):
        c = self.palette[int(i) % self.n]
        return (c[2], c[1], c[0]) if bgr else c

    @staticmethod
    def hex2rgb(h):  # rgb order (PIL)
        return tuple(int(h[1 + i:1 + i + 2], 16) for i in (0, 2, 4))


colors = Colors()


class malaria_inference:
    def __init__(self, modelpath, conf, iou):
        self.modelpath = modelpath
        # self.model = YOLO(modelpath)

        self.conf = conf
        self.iou = iou

    def dectshow(self, boxs, cls, names, zxd):

        label = []
        for i, box in enumerate(boxs):
            id = cls[i]
            x1, y1 = box[0]
            x2, y2 = box[1]
            x3, y3 = box[2]
            x4, y4 = box[3]
            # 创建归一化的xywh格式的边界框
            box_xywh = [int(id), x1, y1, x2, y2, x3, y3, x4, y4, zxd[i]]

            label.append(box_xywh)

            # 获取并显示物体的类别
            # cv2.putText(img, str(names[id]) + ' ' + "{:.2f}".format(zxd[i]),
            #             (int(box[0]), int(box[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        # 显示带注释的图像
        return label

    def convert_coordinates(self,
                            # 输入参数列表，包括检测结果的 TXT 文件路径、输出目录、IoU 阈值等
                            txt_label_path, output_file_dir, iou_threshold, confidence_threshold, area_weight, slice_sep
                            ):
        # txt_file_path: 存放 YOLOv8 小图检测结果的 TXT 文件的上级路径
        # output_file_path: 变换后的结果存放的 TXT 文件路径
        if not os.path.exists(output_file_dir):
            os.makedirs(output_file_dir)
            print(f"Created folder {output_file_dir}")
        output_lines = dict()  # 存储转换后的结果

        # orgimg_w = 0
        # orgimg_h = 0
        # 遍历文件夹中的每个 TXT 文件
        for root, dirs, files in os.walk(txt_label_path):
            for index, filename in enumerate(files):
                # 如果文件以 .txt 结尾，表示它是一个检测结果文件
                if filename.endswith(".txt"):
                    # 获取文件的完整路径
                    filepath = os.path.join(root, filename)

                    # 解析文件名中的信息
                    slice_info = filename.split(".")[0].split(slice_sep)
                    y0 = int(slice_info[-6])
                    x0 = int(slice_info[-5])
                    sliceHeight = int(slice_info[-4])
                    sliceWidth = int(slice_info[-3])
                    orgimg_w = int(slice_info[-2])
                    orgimg_h = int(slice_info[-1])

                    exclude_imgname_char = slice_sep + str(y0) + slice_sep + str(x0) + slice_sep + str(sliceHeight) + \
                                           slice_sep + str(sliceWidth) + slice_sep + str(orgimg_w) + slice_sep + str(
                        orgimg_h)
                    exclude_imgname_index = filename.split(".")[0].index(exclude_imgname_char)
                    imgname = filename.split(".")[0][:exclude_imgname_index]

                    # 读取小图检测结果的坐标信息
                    with open(filepath, "r") as f:
                        lines = f.readlines()

                    # 将边界框坐标转换到原图的坐标空间，并将结果存储到列表中
                    converted_lines = []
                    for line in lines:
                        class_label, x1, y1, x2, y2, x3, y3, x4, y4, conf = line.strip().split(" ")
                        '''
                        x0 和 y0 代表的是图像切片的左上角坐标
                        举个例子，如果原始图像的大小是 3840x2160 像素，你从中切出了一个 640x640 像素的切片，
                        而 (x0, y0) 是 (1000, 1000)，这意味着切片的左上角位于原始图像的坐标 (1000, 1000)。
                        如果在这个切片中检测到一个对象，其坐标 (x, y) 是 (320, 240)，那么在原始图像中，该对象的坐标将是 (1320, 1240)。
                        '''
                        x1_in_original = float(x1) + x0
                        y1_in_original = float(y1) + y0
                        x2_in_original = float(x2) + x0
                        y2_in_original = float(y2) + y0
                        x3_in_original = float(x3) + x0
                        y3_in_original = float(y3) + y0
                        x4_in_original = float(x4) + x0
                        y4_in_original = float(y4) + y0

                        converted_line = [
                            int(class_label),
                            x1_in_original,
                            y1_in_original,
                            x2_in_original,
                            y2_in_original,
                            x3_in_original,
                            y3_in_original,
                            x4_in_original,
                            y4_in_original,
                            float(conf),
                            orgimg_w,
                            orgimg_h
                        ]

                        converted_lines.append(converted_line)
                        # print(converted_lines)

                    # 将转换后的结果添加到输出列表中
                    if imgname not in output_lines.keys():
                        output_lines[imgname] = converted_lines
                    else:
                        output_lines[imgname].extend(converted_lines)

        outputs_file_path_list = []
        for key, value in output_lines.items():
            nms_output_lines = self.apply_nms(
                value,
                iou_threshold,
                confidence_threshold,
                area_weight,
            )

            # 将转换后的结果写入输出文件
            output_file_path = os.path.join(output_file_dir, f"{key}.txt")
            if os.path.exists(output_file_path):
                # import shutil
                import logging
                os.remove(output_file_path)
                logging.warning(
                    f"completed predict txt results of image—{key} have been existed! The original content will be overwritten!")

            with open(output_file_path, "w") as f:
                f.writelines(nms_output_lines)
            print(f"completed predict txt results of image—{key} is saved at: {output_file_path}")
            outputs_file_path_list.append(output_file_path)

        return outputs_file_path_list

    def slice_image(self,
                    image_path,
                    out_dir_all_images,
                    sliceHeight=1280,
                    sliceWidth=1280,
                    overlap=0.1,
                    slice_sep="_",
                    overwrite=True,
                    out_ext=".png",
                    ):
        if len(out_ext) == 0:
            im_ext = "." + image_path.split(".")[-1]
        else:
            im_ext = out_ext

        t0 = time.time()
        image = cv2.imread(image_path)  # , as_grey=False).astype(np.uint8)  # [::-1]
        print("image.shape:", image.shape)

        image_name = os.path.basename(image_path).split('.')[0]
        win_h, win_w = image.shape[:2]

        dx = int((1.0 - overlap) * sliceWidth)
        dy = int((1.0 - overlap) * sliceHeight)

        out_dir_image = os.path.join(out_dir_all_images)

        n_ims = 0
        for y0 in range(0, image.shape[0], dy):
            for x0 in range(0, image.shape[1], dx):
                n_ims += 1

                if (n_ims % 100) == 0:
                    print(n_ims)

                # make sure we don't have a tiny image on the edge
                if y0 + sliceHeight > image.shape[0]:
                    y = image.shape[0] - sliceHeight
                else:
                    y = y0
                if x0 + sliceWidth > image.shape[1]:
                    x = image.shape[1] - sliceWidth
                else:
                    x = x0

                # extract image
                window_c = image[y: y + sliceHeight, x: x + sliceWidth]
                outpath = os.path.join(
                    out_dir_image,
                    image_name
                    + slice_sep
                    + str(y)
                    + "_"
                    + str(x)
                    + "_"
                    + str(sliceHeight)
                    + "_"
                    + str(sliceWidth)
                    + "_"
                    + str(win_w)
                    + "_"
                    + str(win_h)
                    + im_ext,
                )
                if not os.path.exists(outpath):
                    cv2.imwrite(outpath, window_c)
                elif overwrite:
                    cv2.imwrite(outpath, window_c)
                else:
                    print("outpath {} exists, skipping".format(outpath))

        print("Num slices:", n_ims, "sliceHeight", sliceHeight, "sliceWidth", sliceWidth)
        print("Time to slice", image_path, time.time() - t0, "seconds")
        print(
            f"cliped results of {os.path.basename(image_path)} is saved at: {out_dir_image}"
        )
        return out_dir_image

    def calculate_area(self, box):
        """
        计算边界框的面积
        box的格式：[xmin, ymin, xmax, ymax]
        """
        x1, y1, x2, y2, x3, y3, x4, y4 = box
        point1 = (x1, y1)
        point2 = (x2, y2)
        point3 = (x3, y3)
        dis1 = self.calculate_euclidean_distance(point1, point2)
        dis2 = self.calculate_euclidean_distance(point1, point3)
        area = dis1 * dis2
        return area

    def calculate_euclidean_distance(self, point1, point2):
        """
        计算两点之间的欧几里得距离。

        参数:
        point1 (tuple): 第一个点的坐标，格式为 (x1, y1)。
        point2 (tuple): 第二个点的坐标，格式为 (x2, y2)。

        返回:
        float: 两点之间的欧几里得距离。
        """
        x1, y1 = point1
        x2, y2 = point2
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    # def calculate_iou(self, box1, box2):
    #     """
    #     计算两个边界框的IoU（Intersection over Union）
    #
    #     """
    #     x1, y1, x2, y2, x3, y3, x4, y4 = box1
    #     x5, y5, x6, y6, x7, y7, x8, y8 = box2
    #     box1 = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    #     box2 = [(x5, y5), (x6, y6), (x7, y7), (x8, y8)]
    #     # 计算两个多边形的边界框
    #     box1_min_x = min(point[0] for point in box1)
    #     box1_min_y = min(point[1] for point in box1)
    #     box1_max_x = max(point[0] for point in box1)
    #     box1_max_y = max(point[1] for point in box1)
    #
    #     box2_min_x = min(point[0] for point in box2)
    #     box2_min_y = min(point[1] for point in box2)
    #     box2_max_x = max(point[0] for point in box2)
    #     box2_max_y = max(point[1] for point in box2)
    #
    #     # 计算交集的坐标
    #     inter_left = max(box1_min_x, box2_min_x)
    #     inter_top = max(box1_min_y, box2_min_y)
    #     inter_right = min(box1_max_x, box2_max_x)
    #     inter_bottom = min(box1_max_y, box2_max_y)
    #
    #     # 检查交集是否有效
    #     if inter_right < inter_left or inter_bottom < inter_top:
    #         return 0.0
    #
    #     # 计算交集和并集的面积
    #     intersection_area = (inter_right - inter_left) * (inter_bottom - inter_top)
    #     box1_area = (box1_max_x - box1_min_x) * (box1_max_y - box1_min_y)
    #     box2_area = (box2_max_x - box2_min_x) * (box2_max_y - box2_min_y)
    #     union_area = box1_area + box2_area - intersection_area
    #
    #     # 计算IoU
    #     iou = intersection_area / union_area
    #     return iou

    def xyxyxyxy2xywhr(self,box):

        '''
        :param box: 数据要转换成numpy 的格式
        :return:
        '''

        x1, y1, x2, y2, x3, y3, x4, y4 = box
        box = [[x1, y1],[x2, y2],[x3, y3],[x4, y4]]
        box = np.array(box, dtype=np.float32)

        (cx, cy), (w, h), angle = cv2.minAreaRect(box)
        rboxes = [cx, cy, w, h, angle / 180 * np.pi]  # 角度转换为弧度

        return rboxes




    # def vertices_to_xywhr(self, box):
    #     x1, y1, x2, y2, x3, y3, x4, y4 = box
    #     point1=(x1, y1)
    #     point2=(x2, y2)
    #     point3=(x3, y3)
    #
    #     # 计算中心点坐标
    #     x_center = (x1 + x3) / 2
    #     y_center = (y1 + y3) / 2
    #
    #     # 计算宽度和高度
    #     w = self.calculate_euclidean_distance(point1,point2)
    #     h = self.calculate_euclidean_distance(point1,point3)
    #
    #     # 计算旋转角度
    #     v1 = (x2 - x1, y2 - y1)
    #     v2 = (x3 - x1, y3 - y1)
    #     cross_product = v1[0] * v2[1] - v1[1] * v2[0]
    #     dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    #     r = math.atan2(cross_product, dot_product)
    #     box = [x_center, y_center, w, h, r]
    #
    #     return box
    #
    def calculate_iou(self, box1, box2):
        """
        计算两个边界框的IoU（Intersection over Union）

        """

        boxes1 = self.xyxyxyxy2xywhr(box1)
        boxes2 = self.xyxyxyxy2xywhr(box2)

        area1 = boxes1[2] * boxes1[3]
        area2 = boxes2[2] * boxes2[3]
        r1 = ((boxes1[0], boxes1[1]), (boxes1[2], boxes1[3]), boxes1[4])
        r2 = ((boxes2[0], boxes2[1]), (boxes2[2], boxes2[3]), boxes2[4])
        int_pts = cv2.rotatedRectangleIntersection(r1, r2)[1]
        if int_pts is not None:
            order_pts = cv2.convexHull(int_pts, returnPoints=True)
            int_area = cv2.contourArea(order_pts)
            # 计算出iou
            iou = int_area * 1.0 / (area1 + area2 - int_area)
        #        print(int_area)
        else:
            iou = 0




        return iou

    def nms_per_class(self,
                      boxes, scores, classes, iou_threshold, confidence_threshold, area_weight
                      ):
        """
        使用NMS对不同类别的边界框进行后处理
        boxes: 边界框列表，每个边界框的格式为 [xmin, ymin, xmax, ymax]
        scores: 每个边界框的置信度得分列表
        classes: 每个边界框的类别列表
        threshold: 重叠度阈值，高于该阈值的边界框将被抑制
        """
        # 过滤置信度低于阈值的边界框
        filtered_indices = np.where(np.array(scores) >= confidence_threshold)[0]
        boxes = [boxes[i] for i in filtered_indices]
        scores = [scores[i] for i in filtered_indices]
        classes = [classes[i] for i in filtered_indices]

        # 将边界框、置信度、类别转换为NumPy数组
        boxes = np.array(boxes)
        scores = np.array(scores)
        classes = np.array(classes)
        areas = np.array([self.calculate_area(box) for box in boxes])

        # 初始化空列表来存储保留的边界框索引
        keep_indices = []

        # 获取所有唯一的类别标签
        unique_classes = np.unique(classes)

        for cls in unique_classes:
            # 获取属于当前类别的边界框索引
            '''
            classes = np.array([1, 2, 3, 2, 1, 4])
            如果我们想要找出数组中所有类别为 2 的索引，我们可以这样做：
            cls = 2
            cls_indices = np.where(classes == cls)[0]
            print(cls_indices)  # 输出: [1 3]
            在这个例子中，cls_indices 将会是 [1, 3]，因为 classes 数组中索引为 1 和 3 的元素等于 2。
            注意事项：
    np.where(classes == cls)[0] 中的 [0] 是因为 np.where 返回的是一个元组，其中第一个元素包含了满足条件的索引。使用 [0] 来获取这个索引数组。
    如果 cls 在 classes 中不存在，cls_indices 将会是一个空数组。
    这种方法适用于一维数组。如果 classes 是多维的，你可能需要使用不同的索引方式或遍历逻辑。
    np.where 是一个非常有用的函数，可以快速找出满足特定条件的元素位置，它在数据处理和科学计算中非常有用。
            '''
            cls_indices = np.where(classes == cls)[0]

            # 根据当前类别的置信度得分和面积对边界框进行排序
            sorted_indices = np.lexsort(
                (scores[cls_indices], areas[cls_indices] * 1)
            )[::-1]
            # sorted_indices = np.argsort(areas[cls_indices])[::-1]
            cls_indices = cls_indices[sorted_indices]
            while len(cls_indices) > 0:
                # 选择当前得分最高的边界框
                current_index = cls_indices[0]
                current_box = boxes[current_index]
                keep_indices.append(filtered_indices[current_index])

                # 计算当前边界框与其他边界框的IoU
                other_indices = cls_indices[1:]
                ious = np.array(
                    [self.calculate_iou(current_box, boxes[i]) for i in other_indices]
                )

                # 找到重叠度低于阈值的边界框索引
                low_iou_indices = np.where(ious < iou_threshold)[0]

                # 更新剩余边界框索引
                cls_indices = cls_indices[1:][low_iou_indices]
                # cls_indices = low_iou_indices

        return keep_indices

    def apply_nms(self,
                  outputs, iou_threshold, confidence_threshold, area_weight
                  ):
        # 将边界框列表转换为NumPy数组
        outputs = np.array(outputs)

        boxes = []
        scores = []
        class_ids = []
        for out in outputs:
            x1_in_original = out[1]
            y1_in_original = out[2]
            x2_in_original = out[3]
            y2_in_original = out[4]
            x3_in_original = out[5]
            y3_in_original = out[6]
            x4_in_original = out[7]
            y4_in_original = out[8]

            score = out[5]
            class_id = int(out[0])
            orgimg_w = int(out[9])
            orgimg_h = int(out[10])

            class_ids.append(class_id)
            scores.append(score)
            boxes.append(
                [x1_in_original, y1_in_original, x2_in_original, y2_in_original, x3_in_original, y3_in_original,
                 x4_in_original, y4_in_original])

        # 应用NMS
        # indices = cv2.dnn.NMSBoxes(boxes, scores, score_threshold, nms_threshold)
        indices = self.nms_per_class(
            boxes=boxes,
            scores=scores,
            classes=class_ids,
            iou_threshold=iou_threshold,
            confidence_threshold=confidence_threshold,
            area_weight=area_weight,
        )

        # 选择通过NMS过滤后的边界框
        nms_out_lines = []
        for i in indices:
            box = boxes[i]
            score = scores[i]
            class_id = class_ids[i]
            x1 = box[0]
            y1 = box[1]
            x2 = box[2]
            y2 = box[3]
            x3 = box[4]
            y3 = box[5]
            x4 = box[6]
            y4 = box[7]

            nms_out_line = f"{class_id} {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4} {score}\n"
            nms_out_lines.append(nms_out_line)
        return nms_out_lines

    def draw_predictions_on_image(self,
                                  image_path, results_file_path, class_labels, class_names, completed_output_path
                                  ):
        # 确保类别标签和类别名称数量一致
        assert len(class_labels) == len(
            class_names
        ), "Number of class labels should match the number of class names."

        # 读取原图像
        image = cv2.imread(image_path)
        a = []
        boxes_lists = []
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 读取存放变换结果的文本文件
        with open(results_file_path, 'r') as file:
            lines = file.readlines()

        # 遍历每行结果
        for line in lines:
            line = line.strip().split(' ')
            class_label, x1, y1, x2, y2, x3, y3, x4, y4, conf = map(float, line)

            boxes_list = [x1, y1, x2, y2, x3, y3, x4, y4, conf, class_label]
            boxes_lists.append(boxes_list)
            # 获取类别名称和颜色
            classId = class_label
            label = '%.2f' % conf
            label = '%s:%s' % (class_names[int(classId)], label)
            points = [
                [x1, y1],
                [x2, y2],
                [x3, y3],
                [x4, y4]
            ]

            # 将points列表转换为NumPy数组，并调整形状以满足cv2.polylines的要求
            points = np.array(points, dtype=np.int32).reshape((-1, 1, 2))

            # 绘制多边形
            cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)
            print(1)
            # line_thickness = None
            # tl = line_thickness or round(
            #     0.001 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
            #
            # c1, c2 = (x_min, y_min), (x_max, y_max)
            # cv2.rectangle(image, c1, c2, colors(classId, True), thickness=tl + 1, lineType=cv2.LINE_AA, )
            # tf = max(tl, 4)  # font thickness
            # t_size = cv2.getTextSize(label, 0, fontScale=tl / 2, thickness=tf)[0]
            # c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 5
            #
            # if c1[0] + t_size[0] > image_width:
            #     x_over = c1[0] + t_size[0] - image_width
            #     c2 = c1[0] + t_size[0] - x_over, c1[1] - t_size[1] - 5
            #     c1 = x_min - x_over, y_min
            #     cv2.rectangle(image, c1, c2, colors(classId, True), -2, cv2.LINE_AA)  # filled
            #     cv2.putText(image, label, (c1[0], c1[1] - 5), 0, tl / 2,
            #                 [255, 255, 255], 2, lineType=cv2.LINE_AA)
            # else:
            #     cv2.rectangle(image, c1, c2, colors(classId, True), -2, cv2.LINE_AA)  # filled
            #     cv2.putText(image, label, (c1[0], c1[1] - 5), 0, tl / 2,
            #                 [255, 255, 255], 2, lineType=cv2.LINE_AA)

        # image2 = cv2.imread(image_path)
        # if boxes_lists == []:
        #     boxes_lists = np.empty((0, 6))
        # boxes_array = np.array(boxes_lists)
        # a = Results(orig_img=image2, path=image_path, names=class_names, boxes=boxes_array)
        # 保存绘制结果
        filename = os.path.basename(image_path)
        if not os.path.exists(completed_output_path):
            os.makedirs(completed_output_path)

        output_image_path = os.path.join(completed_output_path, filename)
        if os.path.exists(output_image_path):
            # import shutil
            import logging
            os.remove(output_image_path)
            logging.warning(
                f"completed predict visual result of image-{filename} have been existed! The original content will be overwritten!")

        cv2.imwrite(output_image_path, image)
        print(f"completed predict visual result of image-{filename} is saved at: {output_image_path}")

        return a

    def predict(self, images_path):
        outdir_slice_ims = os.path.join(PROJECT_ROOT, 'dataset', 'thin', 'slice_images')
        slice_sep = '_'
        output_file_dir = os.path.join(PROJECT_ROOT, 'results', 'completed_txt')
        iou_threshold = self.iou
        confidence_threshold = self.conf
        area_weight = 1

        completed_output_path = os.path.join(PROJECT_ROOT, 'results', 'completed_predict')

        # 定义图片扩展名列表
        image_extensions = ['.png']
        # image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
        ext = ''

        def is_image_file(path):
            """判断文件是否是图片"""
            return any(path.lower().endswith(ext) for ext in image_extensions)

        if os.path.isfile(images_path) and is_image_file(images_path):
            print(f"{images_path} 是一个图片文件")

            import shutil
            if os.path.exists(outdir_slice_ims):
                shutil.rmtree(outdir_slice_ims)
            os.makedirs(outdir_slice_ims)
            self.slice_image(
                images_path,
                outdir_slice_ims,
                sliceHeight=416,
                sliceWidth=416,
                overlap=0.3,
                slice_sep='_',
                overwrite=False,
                out_ext='.png',
            )
        elif os.path.isdir(images_path):
            print(f"{images_path} 是一个文件夹")
            ext = ''

            im_list = [z for z in os.listdir(images_path) if is_image_file(os.path.join(images_path, z))]

            import shutil
            if os.path.exists(outdir_slice_ims):
                shutil.rmtree(outdir_slice_ims)
            os.makedirs(outdir_slice_ims)
            print(
                f"{os.path.join(outdir_slice_ims)} is existed! The original content will be overwritten!!")
            # slice images
            for i, im_name in enumerate(im_list):
                im_path = os.path.join(images_path, im_name)
                print("=========================== ", im_name, "--", i + 1, "/", len(im_list),
                      " =========================== ")
                self.slice_image(
                    im_path,
                    outdir_slice_ims,
                    sliceHeight=640,
                    sliceWidth=640,
                    overlap=0.3,
                    slice_sep='_',
                    overwrite=False,
                    out_ext='.png',
                )
        else:
            print(f"{images_path} 不是一个有效的文件夹或图片文件")

        yolov8_predict_results_path = os.path.join(PROJECT_ROOT, 'results', 'yolov8_detect', 'predict')

        if os.path.exists(yolov8_predict_results_path):
            import shutil
            import logging
            shutil.rmtree(yolov8_predict_results_path)
            logging.warning(
                f"detect predict path: {yolov8_predict_results_path} is existed! The original content will be overwritten!")

        # -----------------------------------------------------
        path = self.modelpath

        model = YOLO(path)  # pretrained YOLOv8n model
        source = os.path.join(outdir_slice_ims)
        files = os.listdir(source)
        results = []

        for file in files:
            imgpath = os.path.join(source, file)
            results = model(imgpath, save=True, save_txt=True, save_conf=True, conf=0.25, iou=0.25)

            original_dict = results[0].names
            boxes = results[0].obb.xyxyxyxy.cpu().tolist()
            box = []
            zxd = results[0].obb.conf.cpu().tolist()
            cls = results[0].obb.cls.cpu().tolist()
            label = self.dectshow(boxes, cls, original_dict, zxd)
            # 指定保存标签的文件路径
            output_path = r"results/yolov8_detect/predict/labels"
            os.makedirs(output_path, exist_ok=True)  # 确保目录存在

            # 根据文件名生成输出文件的文件名
            output_file = os.path.join(output_path, imgpath.split('\\')[-1].replace('.png', '.txt'))

            # 将标签列表写入到文本文件中
            with open(output_file, 'w') as f:
                for line in label:
                    # 假设每个标签信息使用空格分隔，并且每条信息占一行
                    f.write(f"{' '.join(map(str, line))}\n")

        original_dict = results[0].names
        class_labels = []
        class_names = []
        # 遍历字典，将键赋值给 class_label，将值赋值给 class_names
        for num, name in original_dict.items():
            class_labels.append(int(num))
            class_names.append(name)
        # ----------------------------------------------------------------------------
        txt_label_path = os.path.join(yolov8_predict_results_path, 'labels')

        txt_regress_path_list = self.convert_coordinates(
            txt_label_path=txt_label_path,
            output_file_dir=os.path.join(output_file_dir),
            iou_threshold=iou_threshold,
            confidence_threshold=confidence_threshold,
            area_weight=area_weight,
            slice_sep=slice_sep
        )

        results = []
        if txt_regress_path_list == []:
            image2 = cv2.imread(images_path)
            boxes_lists = np.empty((0, 6))
            boxes_array = np.array(boxes_lists)
            results = Results(orig_img=image2, path=images_path, names=class_names, boxes=boxes_array)


        elif os.path.isfile(images_path) and is_image_file(images_path):
            for txt_regress_path in txt_regress_path_list:
                # image_name = os.path.basename(txt_regress_path).split('.')[0]
                #
                # image_path = os.path.join(image_path, image_name + '.png')
                results = self.draw_predictions_on_image(
                    image_path=images_path,
                    results_file_path=txt_regress_path,
                    class_labels=class_labels,
                    class_names=class_names,
                    completed_output_path=os.path.join(completed_output_path),
                )

        elif os.path.isdir(images_path):
            for txt_regress_path in txt_regress_path_list:
                image_name = os.path.basename(txt_regress_path).split('.')[0]

                im_path = os.path.join(images_path, image_name + '.png')
                results = self.draw_predictions_on_image(
                    image_path=im_path,
                    results_file_path=txt_regress_path,
                    class_labels=class_labels,
                    class_names=class_names,
                    completed_output_path=os.path.join(completed_output_path),
                )

        return results


if __name__ == '__main__':
    modelpath = r'C:\Users\xuzhe\Desktop\First_task\v8_High_resolution\weights\yolov8m-obb.pt'
    pre = malaria_inference(modelpath, conf=0.25, iou=0.1)
    images_path = r'C:\Users\xuzhe\Desktop\First_task\v8_High_resolution\input\P1048.png'

    pres = pre.predict(images_path)

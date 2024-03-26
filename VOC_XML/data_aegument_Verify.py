"""
目的：将原图片(img)与其xml(xml)，合成为打标记的图片(labelled)，矩形框标记用红色即可
已有：（1）原图片文件夹(imgs_path)，（2）xml文件夹(xmls_path)
思路：
    step1: 读取（原图片文件夹中的）一张图片
    step2: 读取（xmls_path）该图片的xml文件，并获取其矩形框的两个对角顶点的位置
    step3: 依据矩形框顶点坐标，在该图片中画出该矩形框
    step4: 图片另存为'原文件名'+'_labelled'，存在‘lablled’文件夹中
"""
import os
import cv2 as cv
import xml.etree.ElementTree as ET
import numpy as np


# 读取中文路径
# def cv_imread(filePath):
#     cv_img = cv.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
#     # imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
#     # cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
#     return cv_img


def xml_jpg2labelled(imgs_path, xmls_path, labelled_path):
    imgs_list = os.listdir(imgs_path)
    xmls_list = os.listdir(xmls_path)
    nums = len(imgs_list)

    print(imgs_list)
    print(xmls_list)

    for i in range(nums):
        img_path = os.path.join(imgs_path, imgs_list[i])
        xml_path = os.path.join(xmls_path, xmls_list[i])

        img = cv.imread(img_path)
        # img = cv.imread(cv_imread(img_path))
        # print('img:',img)

        labelled = img

        # print('img_path:',img_path)
        # print('xml_path:',xml_path)
        # print('labelled:',labelled)

        root = ET.parse(xml_path).getroot()
        objects = root.findall('object')
        for obj in objects:
            bbox = obj.find('bndbox')
            xmin = int(float(bbox.find('xmin').text.strip()))
            ymin = int(float(bbox.find('ymin').text.strip()))
            xmax = int(float(bbox.find('xmax').text.strip()))
            ymax = int(float(bbox.find('ymax').text.strip()))
            # 标注框的设定, (0, 0, 255)为边界框颜色的设定, 5位边界框的宽度设定
            labelled = cv.rectangle(labelled, (xmin, ymin), (xmax, ymax), (0, 0, 255), 5)

        # print('labelled_path:', labelled_path)
        # print('imgs_list[i]:', imgs_list[i])
        # print('%s_labelled.jpg' % (imgs_list[i].split('.')[0]))

        # 保存图片
        # cv.imwrite('%s%s.jpg' % (labelled_path, imgs_list[i]), labelled)
        cv.imwrite('%s/%s_labelled.jpg' % (labelled_path, imgs_list[i].split('.')[0]), labelled)

        # cv.imshow('labelled', labelled)
        # cv.imshow('origin', origin)
        # cv.waitKey()


if __name__ == '__main__':
    # 注意文件路径不能出现中文，否则容易出错
    imgs_path = 'VOC2007/augmented_images'
    xmls_path = 'VOC2007/augmented_annotations'
    labelled_path = 'VOC2007/label_images'
    xml_jpg2labelled(imgs_path, xmls_path, labelled_path)


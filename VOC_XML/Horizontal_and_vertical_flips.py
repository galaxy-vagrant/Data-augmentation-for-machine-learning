import cv2
import numpy as np
import xml.etree.ElementTree as ET
import  os

def augment_flip_images(input_image_folder, input_xml_folder, output_image_folder, output_xml_folder):
    for filename in os.listdir(input_image_folder):
        if filename.endswith('.jpg'):
            # 加载图像和对应的 XML 文件
            image = cv2.imread(os.path.join(input_image_folder, filename))
            tree = ET.parse(os.path.join(input_xml_folder, os.path.splitext(filename)[0] + '.xml'))
            root = tree.getroot()

            # 水平翻转
            flipped_image = cv2.flip(image, 1)

            # 修改 XML 文件中的坐标信息（水平翻转）
            for obj in root.findall('object'):
                bbox = obj.find('bndbox')
                xmin = int(bbox.find('xmin').text)
                xmax = int(bbox.find('xmax').text)
                ymin = int(bbox.find('ymin').text)
                ymax = int(bbox.find('ymax').text)

                new_xmin = image.shape[1] - xmax
                new_xmax = image.shape[1] - xmin

                bbox.find('xmin').text = str(new_xmin)
                bbox.find('xmax').text = str(new_xmax)

            # 保存增强后的图像和修改后的 XML 文件
            output_image_path = os.path.join(output_image_folder, f'flipped_{filename}')
            output_xml_path = os.path.join(output_xml_folder, f'flipped_{os.path.splitext(filename)[0]}.xml')
            cv2.imwrite(output_image_path, flipped_image)
            tree.write(output_xml_path)



def augment_ver_flip_images(input_image_folder, input_xml_folder, output_image_folder, output_xml_folder):
    for filename in os.listdir(input_image_folder):
        if filename.endswith('.jpg'):
            # 加载图像和对应的 XML 文件
            image = cv2.imread(os.path.join(input_image_folder, filename))
            tree = ET.parse(os.path.join(input_xml_folder, os.path.splitext(filename)[0] + '.xml'))
            root = tree.getroot()

            # 竖直翻转
            flipped_image = cv2.flip(image, 0)

            # 修改 XML 文件中的坐标信息（竖直翻转）
            for obj in root.findall('object'):
                bbox = obj.find('bndbox')
                xmin = int(bbox.find('xmin').text)
                xmax = int(bbox.find('xmax').text)
                ymin = int(bbox.find('ymin').text)
                ymax = int(bbox.find('ymax').text)

                new_ymin = image.shape[0] - ymax
                new_ymax = image.shape[0] - ymin

                bbox.find('ymin').text = str(new_ymin)
                bbox.find('ymax').text = str(new_ymax)

            # 保存增强后的图像和修改后的 XML 文件
            output_image_path = os.path.join(output_image_folder, f'vertically_flipped_{filename}')
            output_xml_path = os.path.join(output_xml_folder, f'vertically_flipped_{os.path.splitext(filename)[0]}.xml')
            cv2.imwrite(output_image_path, flipped_image)
            tree.write(output_xml_path)





if __name__ == "__main__":

    input_image_folder = 'VOC2007/JPEGImages'
    input_xml_folder = 'VOC2007/Annotations'
    output_image_folder = 'VOC2007/augmented_images'
    output_xml_folder = 'VOC2007/augmented_annotations'


    augment_flip_images(input_image_folder, input_xml_folder, output_image_folder, output_xml_folder)
    augment_ver_flip_images(input_image_folder, input_xml_folder, output_image_folder, output_xml_folder)


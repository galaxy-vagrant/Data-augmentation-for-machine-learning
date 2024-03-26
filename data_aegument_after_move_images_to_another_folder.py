import os
import shutil


def move_images(source_folder, destination_folder):
    # 确保目标文件夹存在，如果不存在则创建
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 获取源文件夹中的所有文件
    files = os.listdir(source_folder)

    # 遍历文件夹中的所有文件
    for file in files:
        # 检查文件是否为图片文件（假设图片文件以'.jpg'、'.jpeg'、'.png'为扩展名）
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            # 构造源文件路径和目标文件路径
            source_file_path = os.path.join(source_folder, file)
            destination_file_path = os.path.join(destination_folder, file)

            # 移动文件
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved '{file}' to '{destination_folder}'")

if __name__ == '__main__':
    # 指定源文件夹和目标文件夹的路径
    source_folder = '/path/to/source_folder'
    destination_folder = '/path/to/destination_folder'

    # 调用函数移动图片文件
    move_images(source_folder, destination_folder)

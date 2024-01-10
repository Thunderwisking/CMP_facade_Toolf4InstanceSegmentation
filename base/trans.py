import os
import shutil

# 获取当前目录
current_directory = os.getcwd()

# 获取上一级目录
parent_directory = os.path.dirname(current_directory)

# 创建images文件夹和Annotation文件夹（如果不存在的话）
images_directory = os.path.join(parent_directory, 'images')
annotation_directory = os.path.join(parent_directory, 'Annotation')

os.makedirs(images_directory, exist_ok=True)
os.makedirs(annotation_directory, exist_ok=True)

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    if filename.endswith('.jpg'):
        # 如果是.jpg格式图片，复制到images文件夹下
        source_path = os.path.join(current_directory, filename)
        destination_path = os.path.join(images_directory, filename)
        shutil.copy(source_path, destination_path)
    elif filename.endswith('.xml'):
        # 如果是.xml格式文件，复制到Annotation文件夹下
        source_path = os.path.join(current_directory, filename)
        destination_path = os.path.join(annotation_directory, filename)
        shutil.copy(source_path, destination_path)

print("复制完成！")


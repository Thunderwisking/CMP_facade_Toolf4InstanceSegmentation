#### For yg's paper exp
#### For CMP facade dataset
#### To meet the requirements for instance segementation model training
import os
import xml.etree.ElementTree as ET

# 为CMP数据集的每一个标注文件添加根结点
def add_root(file_path):
    if filename.endswith(".xml"):
        with open(xml_path, 'r') as file:
            xml_content = file.read()
            if not xml_content.lower().startswith("<root>"):
                xml_content_with_root = f"<root>\n{xml_content}</root>"
                with open(xml_path, 'w') as file:
                    file.write(xml_content_with_root)



# 处理xml文件
def parse_xml(file_path, output_folder):
    add_root(file_path)
    tree = ET.parse(file_path)
    root = tree.getroot()
    # 遍历每个<object>元素
    for obj_elem in root.findall('object'):
        labelname = obj_elem.find('labelname').text
        print(labelname.strip('\n'))
        if(labelname.strip('\n') == 'window' or labelname.strip('\n') == 'door'):
            point = obj_elem.find('points')
            x = point.findall('x')
            x1 = x[0].text.strip('\n')
            x2 = x[1].text.strip('\n')
            y = point.findall('y')
            y1 = y[0].text.strip('\n')
            y2 = y[1].text.strip('\n')
            output_filename = f"{os.path.split(file_path)[1][:-4]}.txt"
            output_path = os.path.join(output_folder, output_filename)
            with open(output_path, 'a') as file:
                if(labelname.strip('\n') == 'window'):
                    flag = 0
                else:
                    flag = 1
                file.write(f'{flag} {x1} {y1} {x1} {y2} {x2} {y2} {x2} {y1}\n')

            


file_folder = './Annotation'
output_folder = './processed'
for filename in os.listdir(file_folder):
    if filename.endswith(".xml"):
        xml_path = os.path.join(file_folder, filename)
        parse_xml(xml_path, output_folder)
import os
import cv2
import glob
import matplotlib.pyplot as plt
 
def validate_yolo_annotations(images_dir, annotations_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    annotation_files = glob.glob(os.path.join(annotations_dir, '*.txt'))
 
    for annotation_file in annotation_files:
        image_file = os.path.join(images_dir, os.path.splitext(os.path.basename(annotation_file))[0] + '.jpg')
        image = cv2.imread(image_file)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
        with open(annotation_file, 'r') as f:
            lines = f.readlines()
 
        for line in lines:
            data = line.strip().split()
            points = [float(point) for point in data[1:]]
 
            for i in range(0, len(points), 2):
                x = int(points[i] * image.shape[1])
                y = int(points[i + 1] * image.shape[0])
                cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
 
        output_file = os.path.join(output_dir, os.path.basename(image_file))
        cv2.imwrite(output_file, image)
 
        # plt.imshow(image)
        # plt.title(os.path.basename(image_file))
        # plt.show()
 
if __name__ == '__main__':
 
    images_dir = './images'
    annotations_dir = './labels'
    output_dir = './validation'
    validate_yolo_annotations(images_dir, annotations_dir, output_dir)
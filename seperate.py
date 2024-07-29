import os
import shutil


dataset_folder = r"F:\Projects\MaskDetection\Original Data"
labels_folder = os.path.join(dataset_folder, 'yolo_labels')
images_folder = os.path.join(dataset_folder, 'images')
with_annotations_folder = os.path.join(dataset_folder, 'with_annotations')
without_annotations_folder = os.path.join(dataset_folder, 'without_annotations')

os.makedirs(os.path.join(with_annotations_folder, "labels"), exist_ok=True)
os.makedirs(os.path.join(with_annotations_folder, "images"), exist_ok=True)
os.makedirs(os.path.join(without_annotations_folder, "images"), exist_ok=True)

def get_base_filename(file):
    return os.path.splitext(file)[0]

try:
    image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
except FileNotFoundError:
    print(f"Error: The path '{images_folder}' does not exist.")
    exit(1)

label_files = [f for f in os.listdir(labels_folder) if f.lower().endswith('.txt')]

labels_without_extension = set(get_base_filename(label) for label in label_files)

for filename in image_files:
    base_filename = get_base_filename(filename)
    src_image_path = os.path.join(images_folder, filename)
    dest_image_path = os.path.join(without_annotations_folder, "images", filename)
    
    if base_filename in labels_without_extension:
        dest_image_path = os.path.join(with_annotations_folder, "images", filename)
        dest_label_path = os.path.join(with_annotations_folder, "labels", base_filename + '.txt')
        

        shutil.move(src_image_path, dest_image_path)
        
        shutil.move(os.path.join(labels_folder, base_filename + '.txt'), dest_label_path)
    else:
                shutil.move(src_image_path, dest_image_path)

print("Images with annotations and without annotations have been moved to separate folders.")

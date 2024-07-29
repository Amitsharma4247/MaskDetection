import os
import random
import shutil

random.seed(42)

dataset_folder = r"F:\Projects\MaskDetection\Original Data"
with_annotations_folder = os.path.join(dataset_folder, "with_annotations")
labels_folder = os.path.join(with_annotations_folder, 'labels')
images_folder = os.path.join(with_annotations_folder, 'images')
train_folder = os.path.join(dataset_folder, 'train')
validation_folder = os.path.join(dataset_folder, 'val')

os.makedirs(os.path.join(train_folder, 'images'), exist_ok=True)
os.makedirs(os.path.join(train_folder, 'labels'), exist_ok=True)
os.makedirs(os.path.join(validation_folder, 'images'), exist_ok=True)
os.makedirs(os.path.join(validation_folder, 'labels'), exist_ok=True)

def get_base_filename(file):
    return os.path.splitext(file)[0]

image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

label_files = [f for f in os.listdir(labels_folder) if f.lower().endswith('.txt')]

images_with_labels = set(get_base_filename(label) for label in label_files)

images_with_annotations = [img for img in image_files if get_base_filename(img) in images_with_labels]

print(f"Total images with annotations in images folder: {len(images_with_annotations)}")
print("Images with annotations:", images_with_annotations)


random.shuffle(images_with_annotations)


num_samples = len(images_with_annotations)
num_train = int(0.65 * num_samples)
num_validation = num_samples - num_train

train_images = images_with_annotations[:num_train]
validation_images = images_with_annotations[num_train:]


print(f"Number of training images: {len(train_images)}")
print(f"Number of validation images: {len(validation_images)}")

def move_files(files, source_images_folder, source_labels_folder, dest_images_folder, dest_labels_folder):
    for filename in files:
        base_filename = get_base_filename(filename)
        src_image_path = os.path.join(source_images_folder, filename)
        dest_image_path = os.path.join(dest_images_folder, filename)
        
        shutil.copyfile(src_image_path, dest_image_path)
        

        txt_label_filename = base_filename + '.txt'
        src_label_path = os.path.join(source_labels_folder, txt_label_filename)
        dest_label_path = os.path.join(dest_labels_folder, txt_label_filename)
        shutil.copyfile(src_label_path, dest_label_path)

move_files(train_images, images_folder, labels_folder, os.path.join(train_folder, 'images'), os.path.join(train_folder, 'labels'))

move_files(validation_images, images_folder, labels_folder, os.path.join(validation_folder, 'images'), os.path.join(validation_folder, 'labels'))

print("Dataset split into train and validation sets.")

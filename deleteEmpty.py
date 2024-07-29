import os


train_images_path = 'Original Data\\train\\images'
train_labels_path = 'Original Data\\train\\labels'


image_files = os.listdir(train_images_path)

label_files = os.listdir(train_labels_path)

label_file_names = set(os.path.splitext(label)[0] for label in label_files)

image_file_names = set(os.path.splitext(image)[0] for image in image_files)


if len(image_file_names) != len(label_file_names):
    print("There is a discrepancy between the number of image files and label files.")
else:
    print("The number of image files and label files match.")

for image_file in image_files:
    image_name, image_ext = os.path.splitext(image_file)
    
    if image_name not in label_file_names:
        image_path = os.path.join(train_images_path, image_file)
        print(f"Deleting {image_path}")
        os.remove(image_path)

print('Operation completed.')
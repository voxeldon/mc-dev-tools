import os
import random
from PIL import Image
import time

# Define the folder names in the order in which you want to layer the images
folder_names = ['base', 'pants', 'shoes', 'shirt', 'hair']

def get_image_files(folder_path):
    files = []
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)
    return files

number_of_images = int(input("Enter the number of images you wish to generate: "))
base_name = input("Enter the base name of the generated images (default: skin): ") or "skin"

for i in range(number_of_images):
    # Initialize the base image
    base_image = Image.new('RGBA', (64,64), (255,255,255,0))

    # Iterate over the folder names and layer the first image found in each folder
    for folder_name in folder_names:
        folder_path = os.path.join(folder_name)
        files = get_image_files(folder_path)
        if len(files) > 1:
            file_path = random.choice(files)
        else:
            file_path = files[0]
        layer_image = Image.open(file_path)
        base_image.paste(layer_image, (0, 0), layer_image)

    # Save the merged image
    save_name = f"{base_name}_{i}.png"
    base_image.save(save_name)
    print(f"Generated {save_name}")
    time.sleep(0.1)  # To simulate the processing time

while True:
    pass

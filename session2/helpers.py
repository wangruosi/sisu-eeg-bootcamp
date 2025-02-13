import os
import matplotlib.pyplot as plt
from PIL import Image


def display_stim(stimuli_folder):

    # # Set the path to your stimuli folder
    # stimuli_folder = 'stimuli'

    # List and sort all .png files in the stimuli folder
    stimuli_files = [f for f in os.listdir(stimuli_folder) if f.endswith('.png')]
    stimuli_files.sort()

    # Initialize an empty list to store images
    images = []

    # Load images and append to the list
    for file in stimuli_files:
        image_path = os.path.join(stimuli_folder, file)
        image = Image.open(image_path)
        images.append(image)

    # Determine the size of each image
    img_width, img_height = images[0].size

    # Create a new image to hold the montage
    montage_width = img_width * 15
    montage_height = img_height * 4
    montage = Image.new('RGB', (montage_width, montage_height))

    # Paste each image into the montage
    for idx, image in enumerate(images):
        x_offset = (idx % 15) * img_width
        y_offset = (idx // 15) * img_height
        montage.paste(image, (x_offset, y_offset))

    # Display the montage using matplotlib
    plt.figure(figsize=(15, 6))  # Adjust the figure size as necessary
    plt.imshow(montage)
    plt.axis('off')  # Hide axes
    plt.title('All Stimuli')
    plt.show()



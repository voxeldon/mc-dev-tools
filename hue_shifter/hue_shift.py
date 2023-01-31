import os
from PIL import Image

# Take input for the name of the image file, hueS and the number of copies
img_name = input("Enter the name of the image file (default: image.png): ") or "image.png"
hueS = float(input("Enter the value to shift the hue by (default: 22): ") or 22)
hueS = int(hueS)
n_copies = int(input("Enter the number of copies to create (default: 16): ") or 16)

# Check if n_copies is greater than 360 or less than 1
if n_copies > 360:
    n_copies = 360
    print("Number of copies cannot be greater than 360. Value set to 360.")
if n_copies < 1:
    n_copies = 1
    print("Number of copies cannot be less than 1. Value set to 1.")

# Check if the image file exists in the current directory
if os.path.isfile(img_name):
    # Open the image file
    img = Image.open(img_name)
    # Keep the transparency information
    alpha = img.split()[-1] if img.mode == "RGBA" else None
    for i in range(n_copies):
        # Create a copy of the image
        img_copy = img.copy()
        # Adjust the hue of the copy
        img_copy = img_copy.convert("HSV")
        pixels = img_copy.load()
        for x in range(img_copy.width):
            for y in range(img_copy.height):
                r, g, b = pixels[x, y][:3]
                # Slightly change the hue of the pixel
                h = (r + i*hueS) % 360
                pixels[x, y] = (h, g, b)
        img_copy = img_copy.convert("RGBA" if alpha is not None else "RGB")
        # Restore the transparency information if it exists
        if alpha is not None:
            img_copy.putalpha(alpha)
        # Save the copy with a different name
        img_copy.save(img_name.split('.')[0]+ str(i) +"."+img_name.split('.')[1])
    print(f"{n_copies} copies of the image have been created and saved.")
else:
    print("The image file does not exist in the current directory.")

input("Press enter to exit")

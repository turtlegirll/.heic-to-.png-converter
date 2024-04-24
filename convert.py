import os
from PIL import Image
import sys
from pillow_heif import register_heif_opener

# Register HEIF opener, enables Pillow to handle HEIF files
register_heif_opener()

# convert one HEIC file to PNG

def convert_heic_to_png(heic_path, png_path):

    try:
        heic_image = Image.open(heic_path)
        heic_image.save(png_path, 'PNG')
        print(f"Conversion successful. Image saved at {png_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")

# convert all HEIC files in a directory to PNG
def convert_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(directory, filename)
            png_path = os.path.join(directory, filename.rsplit('.', 1)[0] + '.png')
            convert_heic_to_png(heic_path, png_path)
        else:
            print(f"Skipping non-HEIC file: {filename}")

if len(sys.argv) == 2:
    input_directory = sys.argv[1]
    convert_directory(input_directory)
else:
    print("Usage: python convert.py <input_directory>")


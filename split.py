from PIL import Image, ImageDraw
import random
import numpy as np
import argparse
import subprocess

#Remove previous fragments from pixels/ folder
subprocess.run("rm pixels/*", shell=True)

#CL parser
parser = argparse.ArgumentParser(description='Split an image into multiple smaller images')
parser.add_argument('-n', '--num', type=int, default=100, help='number of images to create (default: 100)')
parser.add_argument('-path', '--path', type=str, default="image.jpg", help='image path (default: image.jpg)')
args = parser.parse_args()
num_images = args.num
path = args.path

#open the image and get info
image = Image.open(path).convert("RGBA")
width, height = image.size
total_pixels = width * height
pixels_per_image = total_pixels // num_images

# Create a list of all pixels
all_pixels = [(x, y) for x in range(width) for y in range(height)]
random.shuffle(all_pixels)

# Split the list into chunks
chunks = [all_pixels[i:i + pixels_per_image] for i in range(0, len(all_pixels), pixels_per_image)]

for i, chunk in enumerate(chunks):
  new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
  draw = ImageDraw.Draw(new_image)
  for x, y in chunk:
    draw.point((x, y), fill=(image.getpixel((x,y))))
  new_image.save(f"pixels/output_{i+1}.png")
  print(f"pixels/output_{i+1}.png done!")

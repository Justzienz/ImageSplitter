from PIL import Image
import os 

def run(num):
  image1 = Image.open("pixels/output_1.png")
  image2 = Image.open("pixels/output_2.png")
  result_image = Image.alpha_composite(image1, image2)

  for i in range(3, num+1):
    result_image = Image.alpha_composite(result_image,Image.open(f"pixels/output_{i}.png"))

  result_image.save("final.png")

num_files = len([f for f in os.listdir("pixels") if os.path.isfile(os.path.join("pixels", f))])
run(num_files)

import os
from PIL import Image

factor = 10
image_folder = 'Images'


def scale_up(input_image, output_image):
    image = Image.open(input_image)
    width, heidth = image.size
    scaled_image = image.resize((width*factor, heidth*factor), resample=Image.NEAREST)
    scaled_image.save(output_image)
    # os.remove(input_image)


files = os.listdir(image_folder)

for file in files:
    if not file.startswith('IMG_'): continue
    if '_scale_x' in file: continue
    output = file.split('.')
    output = f'{output[0]}_scale_x{factor}.png'
    output = os.path.join(image_folder, output)
    file = os.path.join(image_folder, file)
    scale_up(input_image=file, output_image=output)

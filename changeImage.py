#!/usr/bin/env python3

import os
from PIL import Image

img_src = "./supplier-data/images/"
img_lst = os.listdir(img_src)
size = (600, 400)

for img in img_lst:
    img_o = img.split('.')[0] + '.jpeg'
    try:
        with Image.open(img_src + img) as img_file:
            new_img = img_file.convert('RGB')
            new_img = new_img.resize(size)
            new_img.save(img_src + img_o, 'JPEG')
    except OSError:
        print("cannot convert", img)

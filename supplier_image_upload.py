#!/usr/bin/env python3

import requests
import os

url = "http://104.197.0.227/upload/"
img_src = "./supplier-data/images/"
img_lst = os.listdir(img_src)

for img in img_lst:
    if img.find(".jpeg") >= 0:
        try:
            with open(img_src + img, 'rb') as img_file:
                r = requests.post(url, files={'file': img_file})
        except OSError:
            print("Error")

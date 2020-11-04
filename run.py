#! /usr/bin/env python3

import os
import requests
import json

url = "http://104.197.0.227/fruits/"
path = "./supplier-data/descriptions/"
files = os.listdir(path)
for file in files:
    name = file.split('.')[0] + '.jpeg'
    with open(path + file) as dcp_file:
        lines = dcp_file.readlines()
        dct = {
            "name": lines[0].strip(),
            "weight": int(lines[1].strip().split()[0]),
            "description": lines[2].strip(),
            "image_name": name
        }
        response = requests.post(url, json=dct)
        print(response.ok)
        print(dct)
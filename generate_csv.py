#!/usr/bin/python

import os
import sys
import pandas as pd

files_dict = dict()
path = r'C:\Users\brijesh kumar\Desktop\cartisan_Brijesh_Kumar_Ex_2\ikea-webscrapper-script\test.csv'
data = {
    'filename': [],
    'label': []
}

for root, dirs, files in os.walk(r"C:\Users\brijesh kumar\Desktop\cartisan_Brijesh_Kumar_Ex_2\ikea-webscrapper-script\Train\images\test"):
    for filename in files:
        print(filename)
        if "table" in filename:
            data['filename'].append(filename)
            data['label'].append(0)
        elif "chair" in filename:
            data['filename'].append(filename)
            data['label'].append(1)
        elif "bed" in filename:
            data['filename'].append(filename)
            data['label'].append(2)
        elif "lighting" in filename:
            data['filename'].append(filename)
            data['label'].append(3)
        else:
            raise ValueError("Invalid Filename")

df1 = pd.DataFrame(data)
df1.to_csv(path, index=False)

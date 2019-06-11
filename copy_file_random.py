import shutil, random
import os

dirpath = r'C:\Users\brijesh kumar\Desktop\cartisan_Brijesh_Kumar_Ex_2\ikea-webscrapper-script\images'
destDirectory = r'C:\Users\brijesh kumar\Desktop\cartisan_Brijesh_Kumar_Ex_2\ikea-webscrapper-script\test'

filenames = random.sample(os.listdir(dirpath), 200)
for fname in filenames:
    srcpath = os.path.join(dirpath, fname)
    shutil.copy(srcpath, destDirectory)

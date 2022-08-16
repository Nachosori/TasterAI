from calendar import c
from PIL import Image
import numpy as np
from os import listdir
from matplotlib import pyplot as plt

dir_classes = "/meta/classes.txt"
read_classes = open(dir_classes, "r")
with read_classes as archivo:
    classes = list(map(str.rstrip, archivo))




X,y = [], []
for folder in classes:
    images = listdir(f"/images/{folder}")
    for image in images:
        if image == ".DS_Store":
            continue
        path = f"/images/{folder}/{image}"
        size = (160,160)
        img = Image.open(path).resize(size).convert("RGB")
        img = np.array(img)
        img = img/255
        X.append(img)
        y.append(folder)


X,y = np.array(X),np.array(y)

np.save("/array/X.npy", X)
np.save("/array/y.npy", y)
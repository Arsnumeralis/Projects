import os
from PIL import Image, ImageFilter
import sys

path_old = (sys.argv[1])

if os.path.isdir(sys.argv[2]) == True:
    path_new = (sys.argv[2])
else:
    os.mkdir(sys.argv[2])
    path_new = (sys.argv[2])

for filename in os.listdir(path_old):
    if filename.endswith(".jpg"):
        img = Image.open(path_old + "\\" + filename)
        img.save(path_new + "\\" + filename[0:-4] + ".png", "png")

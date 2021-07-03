import os
from time import time
from PIL import Image, ImageFilter
import sys

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} seconds to run this program')
        return result
    return wrapper

# grab args 1 and 2
# check if arg 2 folder exists, if not create

path_old = (sys.argv[1])

if os.path.isdir(sys.argv[2]) == True:
    path_new = (sys.argv[2])
else:
    os.mkdir(sys.argv[2])
    path_new = (sys.argv[2])


# loop through arg1 folder


for filename in os.listdir(path_old):
    if filename.endswith(".jpg"):
        img = Image.open(path_old + "\\" + filename)
        img.save(path_new + "\\" + filename[0:-4] + ".png", "png")

# convert them to png
# save them into the arg2 folder




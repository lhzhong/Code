# python三种方式读取图片

import time
import numpy as np
import cv2
from scipy import misc
from skimage import io
from PIL import Image
import matplotlib.image as mpimg
N = 1000

# 1.opencv读取
tic1 = time.time()
for i in range(N):
    img = cv2.imread("lena.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(type(img))
print("opencv读取效率：每秒{}张\n".format(int(N / (time.time() - tic1))))

# 2.scipy读取
tic2 = time.time()
for i in range(N):
    img = misc.imread("lena.png")
print(type(img))
print("scipy读取效率：每秒{}张\n".format(int(N / (time.time() - tic2))))

# 3.skimage读取
tic3 = time.time()
for i in range(N):
    img = io.imread("lena.png")
print(type(img))
print("skimage读取效率：每秒{}张\n".format(int(N / (time.time() - tic3))))

# 4.pillow读取
tic4 = time.time()
for i in range(N):
    img = Image.open("lena.png")
    img = np.array(img)  # 转换花费时间
print(type(img))
print("pillo读取效率：每秒{}张\n".format(int(N / (time.time() - tic4))))

# 5.matplotlib读取
tic5 = time.time()
for i in range(N):
    img = mpimg.imread("lena.png")
print(type(img))
print("matplotlib读取效率：每秒{}张\n".format(int(N / (time.time() - tic5))))
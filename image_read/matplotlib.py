import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
from scipy.misc import imresize

# 读取图片，读取得到的是uint8类型的数组
lena = mpimg.imread('lena.jpeg')
plt.imshow(lena)
plt.show()

＃转化为灰度图像，matplotlib 中没有合适的函数可以将 RGB 图转换为灰度图，用公式自定义
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
gray = rgb2gray(lena)
plt.imshow(gray, cmap='Greys_r')
plt.show()

＃图像缩放
lena_new_sz = imresize(lena, (224,224)) # 第二个参数如果是整数，则为百分比，如果是tuple，则为输出图像的尺寸
plt.imshow(lena_new_sz)
plt.show()

＃保存图像
misc.imsave('lena_new_sz.png', lena_new_sz)
plt.savefig('lena_new_sz.png')

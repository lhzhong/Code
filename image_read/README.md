# python/tensorflow 读取图片的几种方式

### 1.matplotlib

### 2.PIL.Image

由于PIL.Image和matplotlib各有优势，所以有时会经常转换使用，因matplotlib读取的是数组形式，而PIL.Image又有转灰度图的直接函数，以下代码几位混合使用


```
import matplotlib.pyplot as plt 
import numpy as np
from scipy.misc import imresize
from PIL import Image

# 读取图片，读取得到的是uint8类型的数组
frame = Image.open('lena.jpeg')

frame = Image.fromarray(np.array(frame))
frame = frame.convert("L")
frame = np.array(frame.getdata(),
                 dtype=np.uint8).reshape((400, 400))
frame = imresize(frame, (224, 224))
plt.imshow(frame, cmap='Greys_r')
plt.show()
```
### 3.opencv读取
opencv需要另外安装 
安装执行```conda install -c menpo opencv3```

```
# 读取图片，保存的是unit8类型数组
import cv2
frame = cv2.imread('lena.jpeg')
```
### 4.tensorflow读取
tensorflow可用```tf.gfile.FastGFile('lena.jpeg', 'rb').read()```和```tf.image.decode_jpeg()```读取和解压图片，但我测试了一下tensorflow解压出来的图片都是三个通道的，即使我读进去的是一通道的图片，其也会将它转化为3通道，所以要得到灰度图，在读取解压后还需要再转换

https://blog.csdn.net/uestc_c2_403/article/details/74156830

https://www.cnblogs.com/yinxiangnan-charles/p/5928689.html

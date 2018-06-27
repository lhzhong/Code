from PIL import Image

# 读取图片，读取到的是Image类型的数据，并非数组类型
# 显示图片时，可能无法显示，在ubuntu下安装　sudo apt-get install imagemagick
lena = Image.open('lena.png')
lena.show()

# 转化为灰度图
gray = lena.convert('L')
gray.show()

＃ 图像缩放
lena_new_sz = lena.resize((224,224))
lena_new_sz.show()

＃ 保存图像
I.save('lena_new_sz.png')

# PIL Image 图片和 numpy 数组互相转换
lena_array = np.array(lena)      # PIL Image图片转换为numpy数组
im = Image.fromarray(lena_array) # numpy数组转换为PIL Image图片

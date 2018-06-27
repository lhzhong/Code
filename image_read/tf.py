import matplotlib.pyplot as plt
import tensorflow as tf

with tf.Session() as sess:  
    image = tf.gfile.FastGFile('lena.jpeg', 'rb').read()  　　　　 # 读取图片
    image = tf.image.decode_jpeg(image) 　　　　　　　　　　　　　　  # image_data为tensor形式
    image = tf.image.rgb_to_grayscale(image)                　　　# 转换为灰度图
    image = tf.image.resize_images(image, [224, 224], method=0)
    image = tf.image.per_image_standardization(image)
    image = sess.run(image)
    plt.imshow(image[:,:,0],cmap ='gray') 
    plt.savefig('new_lena.jpeg')
    plt.show() 
    

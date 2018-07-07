"""
tf.shape(a)和a.get_shape()比较:
    tf.shape()中a 数据的类型可以是tensor, list, array
    a.get_shape()中a的数据类型只能是tensor,且返回的是一个元组（tuple）
"""

import tensorflow as tf

x = tf.constant([[1, 2, 3], [4, 5, 6]])
y = [[1, 2, 3], [4, 5, 6]]

sess = tf.Session()

# tf.shape()
x_shape1 = tf.shape(x)
y_shape1 = tf.shape(y)
print(sess.run(x_shape1))       # output: [2,3]
print(sess.run(y_shape1))       # output: [2,3]

# a.get_shape()
print(x.get_shape())            # output: (2, 3)
print(x.get_shape().as_list())  # output: [2,3]
print(y.get_shape())            # AttributeError: 'list' object has no attribute 'get_shape'

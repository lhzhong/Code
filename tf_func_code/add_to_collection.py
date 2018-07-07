"""
tf.add_to_collection：把变量放入一个集合，把很多变量变成一个列表
tf.get_collection：从一个结合中取出全部变量，是一个列表
tf.add_n：把一个列表的东西都依次加起来
"""

import tensorflow as tf

# tf.constant_initizlizer 可以简写成tf.constant()
a = tf.get_variable('a', initializer=tf.constant_initializer(2))
b = tf.get_variable('b', initializer=tf.constant_initializer(4))

tf.add_to_collection('losses', a)
tf.add_to_collection('losses', b)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
ab = tf.get_collection('losses')
c = tf.add_n(tf.get_collection('losses'))

# output: [2,4]
print(sess.run(ab))
# output: 6
print(sess.run(c))

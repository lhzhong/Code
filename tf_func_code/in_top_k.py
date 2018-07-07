"""
tf.nn.in_top_k( predictions, targets, k, name=None)
Args:
    predictions: A Tensor of type float32. A batch_size x classes tensor.
    targets: A Tensor. Must be one of the following types: int32, int64. A batch_size vector of class ids.
    k: An int. Number of top elements to look at for computing precision.
    name: A name for the operation (optional).
Return:
    A Tensor of type bool.
Notice:
    If multiple classes have the same prediction value and straddle the top-k boundary,
    all of those classes are considered to be in the top k

tf.equal(x, y, name=None)
Args:
    x: A Tensor. Must be one of the following types: bfloat16, half, float32, float64, uint8, int8, int16, int32, int64,
        complex64, quint8, qint8, qint32, string, bool, complex128.
    y: A Tensor. Must have the same type as x.
    name: A name for the operation (optional).
Return:
    A Tensor of type bool.
Notice:
    If two elements are equal, the lower-index element appears first.
"""

import tensorflow as tf

predict = tf.constant([[0, 0, 0], [1, 1, 1]], dtype=tf.float32)
label = tf.constant([2, 1], dtype=tf.int32)

result1 = tf.nn.in_top_k(predict, label, 1)
result2 = tf.equal(tf.cast(tf.argmax(predict, 1), tf.int32), label)

sess = tf.Session()

# [True, True]
print(sess.run(result1))
# [False, False]
print(sess.run(result2))









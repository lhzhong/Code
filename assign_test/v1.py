#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:39:35 2018

@author: zhong
"""

import tensorflow as tf
import numpy as np
import time
with tf.Graph().as_default():
    v1 = tf.get_variable('l_enc', [40000,1024])
    v2 = tf.get_variable('l_dec', [40000,1024])
    
    start_time = time.time()
    
    init_op = tf.global_variables_initializer()
    
    saver = tf.train.Saver()
    i=0
    with tf.Session() as sess:
        sess.run(init_op)
        for v in tf.trainable_variables():
            print(i)
            embedding = np. random.uniform(-1, 1, (40000, 1024))
            sess.run(v.assign(embedding))
            print(sess.run(v))
            i = i+1
            
            save_path = saver.save(sess, './v1/model.ckpt')
        print('time:%ss'%(time.time()-start_time))

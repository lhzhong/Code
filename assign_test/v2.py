#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:26:29 2018

@author: zhong
"""
import tensorflow as tf
import numpy as np
import time
with tf.Graph().as_default():
    v1 = tf.get_variable('l_enc', [40000,1024])
    v2 = tf.get_variable('l_dec', [40000,1024])
    varss = [v1, v2]
    
    start_time = time.time()
    
    placeholders = [tf.placeholder(tf.float32, shape=[40000, 1024]) for v in varss]
    assign_ops = [v.assign(p) for (v,p) in zip(varss, placeholders)]
    
    init_op = tf.global_variables_initializer()
    
    saver = tf.train.Saver()
    
    with tf.Session() as sess:
        sess.run(init_op)
        for p, assign_op in zip(placeholders, assign_ops):
            embedding = np. random.uniform(-1, 1, (40000, 1024))
            result = sess.run(assign_op, {p:embedding})
            print(result)
            save_path = saver.save(sess, './v2/model.ckpt')
        print('time:%ss'%(time.time()-start_time))
        

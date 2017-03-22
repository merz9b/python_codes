import tensorflow as tf
import numpy as np


class LinearRegressor(object):
    def __init__(self,x,y,const = True):
        '''
        :param x:  测量值
        :param y: 目标值
        :param const: 是否有常数项
        '''
        self.y = y
        self.x = x
        self._loss = []
    @staticmethod
    def add_constant(x, axis=1):
        '''
        :param x: np.ndarry
        :return: add a columns of 1 to x
        '''
        nr, nc = x.shape
        if axis == 1:
            const = np.ones((nr, 1)).astype(x.dtype)
        else:
            const = np.ones((1, nc)).astype(x.dtype)
        return np.concatenate([const, x], axis=axis)
    def train(self):
        x1 = self.x.T
        x = LinearRegressor.add_constant(x1,axis=0)
        nr,nc = x.shape
        b = tf.Variable(tf.random_uniform([1, nr]))  # 待估系数
        y = tf.matmul(b, x)  # y：估计输出
        # 最小化方差
        loss = tf.reduce_mean(tf.square(y - self.y))
        optimizer = tf.train.GradientDescentOptimizer(0.1)  # learn rate = 0.5
        train = optimizer.minimize(loss)
        # 初始化变量
        init = tf.global_variables_initializer()
        # 启动图 (graph)
        sess = tf.Session()
        sess.run(init)
        for step in range(0, 10000):
            sess.run(train)
            self._loss.append(sess.run(loss))
            if step % 1000 == 0:
                print('Step %s : \nBeta : %s' % (step, sess.run(b)))
        self.coef = b.eval(sess)
    def pred(self):
        return self.coef
    @property
    def loss_curve(self):
        return self._loss

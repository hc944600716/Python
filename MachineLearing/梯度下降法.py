# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/20 16:35
@Auth ： victory.He
@File ：梯度下降法.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""
import random

import matplotlib.pyplot as plt
import numpy as np

"""
:EPS =平均误差

"""
lr = 0.123  # 学习率
epochs = 1000  # 最大遍历次数
w = 0  # 权重
b = 0  # 偏差


def rd() -> "该函数 用于随机生成 -1 和 1 之间的数  不含0  relu":
    x = random.randint(-2, 2)
    if (x != -1 and x != 1):
        return rd()
    else:
        return x


# 随机生成 w,b 取值为 -1,1(不包含0);
w = np.random.random() * rd()
b = np.random.random() * rd()

print("生成的w {} \t b {}".format(w, b))


def date_generate() -> "用于生成一个正态分布数据集":
    point_num = 1000
    vectors_set = []
    for vector in range(point_num):
        x1 = np.random.normal(0.0, 0.9)
        y1 = x1 * 0.5 + 0.3 + np.random.normal(0.0, 0.5)
        vectors_set.append([x1, y1])
        plt.scatter(x1, y1)
    plt.show()
    return vectors_set


def split_x_y(train_date, test_date):
    x_train = [d[0] for d in train_date]
    y_train = [d[1] for d in train_date]
    x_test = [d[0] for d in test_date]
    y_test = [d[1] for d in test_date]
    return x_train, y_train, x_test, y_test


def split_date(vectors_set) -> "拆分数据集 xi yi ":
    vectors_set = np.array(vectors_set)

    test_num = int(len(vectors_set) * 0.2)
    x_data = []
    test_date = vectors_set[:test_num]
    train_date = vectors_set[test_num:]
    y_data = []
    for i in vectors_set:
        x_data.append((i)[0])
        y_data.append((i)[1])
        pass
    return train_date, test_date


def loss_date(vectors_set, y_date, x_date, w, b) -> "vectors_set 数据集 , y_date 真实值集合 ,x_date 训练值参数 ":
    loss = 0
    avg_loss = 0.0
    for i in range(len(y_date)):
        loss += ((w * x_date[i] + b) - y_date[i]) ** 2
        pass
    avg_loss = loss / len(y_date)
    return avg_loss / 2.0  # 返回损失值


def Train(vectors_set, w, b, x_train, y_train, x_test, y_test):  # 更新   w , b
    count = 0
    n = float(len(x_train))
    for i in range(epochs):  # 循环训练epochs次
        b_grad = 0
        w_grad = 0
        for j in range(0, len(x_train)):
            b_grad += (1 / n) * (((w * x_train[j]) + b) - y_train[j])
            w_grad += (1 / n) * x_train[j] * (((w * x_train[j]) + b) - y_train[j])
        b = b - (lr * b_grad)
        w = w - (lr * w_grad)
        train_avg_loss = loss_date(vectors_set, y_train, x_train, w, b)
        test_avg_loss = loss_date(vectors_set, y_test, x_test, w, b)
        count += 1
        print('第{}轮 更新后的 w:{}\t\tb:{} \t\t train_loss_avg={}\t test_loss_avg={}'.format(count, w, b, train_avg_loss,
                                                                                        test_avg_loss))

    return w, b


def draw(x_date, y_date, w, b) -> "绘图":
    x = x_date
    y = []
    plt.scatter(x_date, y_date)
    for i in x_date:
        y.append(i * w + b)
    plt.plot(x, y, color="r")
    plt.show()


def run(w, b):
    vectors_set = date_generate()
    train_date, test_date = split_date(vectors_set)
    x_train, y_train, x_test, y_test = split_x_y(train_date, test_date)
    w, b = Train(vectors_set, w, b, x_train, y_train, x_test, y_test)
    draw(x_train, y_train, w, b)
    draw(x_test, y_test, w, b)

    pass


if __name__ == "__main__":
    run(w, b)

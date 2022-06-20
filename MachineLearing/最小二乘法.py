# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/20 16:22
@Auth ： victory.He
@File ：最小二乘法.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""
import numpy as np
import matplotlib.pyplot as plt
import math


#生成数据
num = 200
x=[] #升高列表
y=[] #体重列表
for i in range(num):
    x_temp=np.random.normal(loc=170,scale=5.0)
    x.append(x_temp)
    y_temp=x_temp - 105 + np.random.normal(loc=0, scale=2.0)
    y.append(y_temp)
    plt.scatter(x=x,y=y)
plt.show()
X = np.array(x)
Y = np.array(y)


# # 身高数据
# x = np.array([162, 165, 159, 173, 157, 175, 161, 164, 172, 158])
# # 体重数据
# y = np.array([48, 64, 53, 66, 52, 68, 50, 52, 64, 49])



# 返回R平方
def computeCorrelation(X, Y):
    xBar = np.mean(X)    #平均值
    yBar = np.mean(Y)
    SSR = 0
    varX = 0
    varY = 0
    for i in range(0, len(X)):
        diffXXBar = X[i] - xBar
        diffYYBar = Y[i] - yBar
        SSR += (diffXXBar * diffYYBar)
        varX += diffXXBar ** 2
        varY += diffYYBar ** 2

    SST = math.sqrt(varX * varY)
    return math.pow((SSR / SST), 2)


# 返回回归方程
def regression(x, y):
    x_mean = np.mean(x)  # x平均值
    y_mean = np.mean(y)  # y平均值
    num = 0.0  # 分子∑
    d = 0.0  # 分母∑
    for x_i, y_i in zip(x, y):
        num += (x_i - x_mean) * (y_i - y_mean)
        d += (x_i - x_mean) ** 2
    a = num / d  # 根据公式得到a
    b = y_mean - a * x_mean  # 根据公式得到b
    fangcheng = "y=" + str(a) + "*x" + str(b)
    return fangcheng, a, b


fangcheng, a, b = regression(x, y)

print(" 求得方程：", fangcheng, "  R²=", computeCorrelation(x, y))

# print(type(a),type(b),type(x))
y_hat = a * X + b  # 回归方程
plt.scatter(x, y)  # 描点
plt.plot(x, y_hat, color='r')  # 画线
plt.axis()  # 设置坐标上下限
plt.show()  # 显示


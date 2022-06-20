# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/20 18:41
@Auth ： victory.He
@File ：KNN.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""

import numpy as np
from matplotlib import pyplot as plt

x_date_num = 30
y_date_num = 30
z_date_num = 30

x = np.random.normal(0, 2, x_date_num)
y = np.random.normal(5, 4, y_date_num)
z = np.random.normal(9, 6, z_date_num)

x1 = np.random.uniform(0, 2, (1, x_date_num))
y1 = np.random.uniform(5, 4, (1, y_date_num))
z1 = np.random.uniform(9, 6, (1, z_date_num))

# 设置默认字体为中文
# plt.rcParams["font.family"] = "SimHei"
plt.scatter(x, x1, color="r", label="x")
plt.scatter(y, y1, color="g", label="y")
plt.scatter(z, z1, color="b", label="z")
# 默认位置， 使用默认字体
plt.legend()

plt.show()

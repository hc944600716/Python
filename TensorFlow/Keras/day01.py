# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/21 9:15
@Auth ： victory.He
@File ：day01.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""
import  numpy as np
import matplotlib.pyplot as  plt
from keras.models import Sequential as st
from  keras.layers import  Dense
def gennerate_date():
    num=1000
    vectors_set= []
    for i in range(num):
        x1 =np.random.normal(0.0,0.9)
        y1 =x1*0.5 +0.3 + np.random.normal(0.0,0.5)
        vectors_set.append([x1,y1])
    return [v[0] for v in vectors_set],[v[1] for v in vectors_set]




def hidden_layer(x_date,y_date):
    model=st()
    model.add(Dense(1,input_dim=1,activation=None))
    model.compile(loss="MSE",optimizer='sgd',metrics=['accuracy'])
    Train(model,x_date,y_date)
    predict_y=model.predict(x_date)
    return predict_y

def Train(model,x_date,y_date):
    model.fit(x=x_date,y=y_date,batch_size=10,epochs=10)

def draw(x_date,y_date,predict_y):
    plt.scatter(x_date,y_date)
    plt.plot(x_date,predict_y,color="r")
    plt.show()
    pass

def run():
    x_date,y_date=gennerate_date()
    predict_y=hidden_layer(x_date,y_date)
    draw(x_date,y_date,predict_y)
    pass
if __name__ =="__main__":
    run()
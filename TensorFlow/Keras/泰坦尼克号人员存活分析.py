# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/25 11:07
@Auth ： victory.He
@File ：泰坦尼克号人员存活分析.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""
import pandas as pd
from keras.models import Sequential as st
from keras.layers import  Dense
import numpy as np
import tensorflow as tf
import os
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
tf.device("gpu")
Train_date=pd.read_csv("../date/train .csv")
Test_date=pd.read_csv("../date/test.csv")

#数据处理
Train_date_copy=Train_date.copy()
Train_date_copy=Train_date_copy.dropna(subset=["Age","Sex","Embarked","Fare"])

Train_date_copy.Sex=Train_date_copy.Sex.replace(["male","female"],value=[0,1])

Train_date_copy.Embarked=Train_date_copy.Embarked.replace(["S","C","Q"],value=[0,1,2])
Train_date_copy=Train_date_copy.drop(columns=["Name","Ticket","Cabin","PassengerId"])

# print(Train_date_copy.to_string())






Test_date_copy=Test_date.copy()
Test_date_copy=Test_date_copy.dropna(subset=["Age","Sex","Embarked","Fare"])

Test_date_copy.Sex=Test_date_copy.Sex.replace(["male","female"],value=[0,1])

Test_date_copy.Embarked=Test_date_copy.Embarked.replace(["S","C","Q"],value=[0,1,2])
Test_date_copy=Test_date_copy.drop(columns=["Name","Ticket","Cabin","PassengerId"])


def To_list(date):
    Survived,Pclass,Sex,Age,SibSb,Fare,Embarked = date["Survived"],date["Pclass"],date["Sex"],date["Age"],date["SibSp"],date["Fare"],date["Embarked"]
    return Survived,Pclass,Sex,Age,SibSb,Fare,Embarked


# TrainDate=[Train_date_copy["Pclass"] ,Train_date_copy["Sex"],Train_date_copy["Age"] ,Train_date_copy["SibSp"] ,
#                  Train_date_copy["Parch"] ,Train_date_copy["Fare"] ,Train_date_copy["Embarked"] ]
# TrainDate=tf.convert_to_tensor(TrainDate)
# print(TrainDate)
#
# TrainDate_Lable=tf.convert_to_tensor(Train_date_copy["Survived"])
# print(TrainDate_Lable)
# TestDate=tf.convert_to_tensor([Test_date_copy["Pclass"] ,Test_date_copy["Sex"],Test_date_copy["Age"] ,Test_date_copy["SibSp"] ,
#                  Test_date_copy["Parch"] ,Test_date_copy["Fare"] ,Test_date_copy["Embarked"]])

# TestDate_Lable=tf.convert_to_tensor(Test_date_copy["Survived"])

Train_lable=Train_date_copy.pop("Survived")
# Train_date=tf.convert_to_tensor(Train_date_copy)



#构建神经网络骨架

model=st()
model.add(Dense(128,input_dim=7,input_shape=(7,),activation="relu"))
model.add(Dense(64,input_dim=128,activation="tanh"))

model.add(Dense(32,activation="tanh"))
model.add(Dense(24,activation="tanh"))
model.add(Dense(12,activation="tanh"))

model.add(Dense(1,input_dim=12,activation="tanh"))
history=model.compile(loss="MSE",optimizer='Adam',metrics=['accuracy'])

"""
softmax：对输入数据的最后一维进行softmax，输入数据应形如(nb_samples, nb_timesteps, nb_dims)或(nb_samples,nb_dims)

elu

selu: 可伸缩的指数线性单元（Scaled Exponential Linear Unit），参考Self-Normalizing Neural Networks

softplus

softsign

relu

tanh

sigmoid

Sigmoid函数由下列公式定义  
Sigmoid 曲线
hard_sigmoid

linear 

"""
"""optimizer

Adadelta、Adagrad、Adam、RMSprop


"""
"""loos:  MSE 
        mean_squared_error
        mean_absolute_error
        mean_absolute_percentage_error
        mean_squared_logarithmic_error
        squared_hinge
        hinge
        categorical_hinge
        logcosh
        categorical_crossentropy
        sparse_categorical_crossentropy
        binary_crossentropy
        kullback_leibler_divergence
        poisson
        cosine_proximity     """
model.summary()
model.fit(x=Train_date_copy,y=Train_lable,batch_size=40,epochs=1000,)  #20 0.93  45 4000 0/96
# model.evaluate(Test_date)
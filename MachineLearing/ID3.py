# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/20 18:24
@Auth ： victory.He
@File ：ID3.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""
# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/11 10:46
@Auth ： victory.He
@File ：test.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""
import copy
import time
from math import log
import operator
import pandas as pd
import os
import json
import matplotlib.pyplot as plt

def create_date():
    lable = ["age", "income", "student", "credit_rating", "Class:buys_computer"]
    date = [["Youth", "high", "No", "Fair", "No"],
            ["Youth", "high", "No", "excellent", "No"],
            ["middle_age", "high", "No", "Fair", "Yes"],
            ["Senior", "medium", "No", "Fair", "Yes"],
            ["Senior", "high", "yes", "Fair", "Yes"],
            ["Senior", "high", "yes", "excellent", "No"],
            ["middle_age", "midium", "yes", "excellent", "Yes"],
            ["Youth", "high", "No", "Fair", "No"],
            ["Youth", "high", "yes", "Fair", "Yes"],
            ["Senior", "medium", "yes", "Fair", "Yes"],
            ["Youth", "medium", "yes", "excellent", "Yes"],
            ["middle_age", "medium", "No", "excellent", "Yes"],
            ["middle_age", "high", "yes", "fair", "Yes"],
            ["Senior", "medium", "NO", "excellent", "No"],
            ]
    return date,lable


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # 求|D|=14   K数据标签：几种结果最终   |Ck|怎么实现
    """实现  |ck|"""
    labelCounts = {}  # 空字典  a={yes：9}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        # print(currentLabel)
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        """实现ck"""

    shannonEnt = 0.0  # 香农熵初始值
    """实现表达式的构建求和"""
    for key in labelCounts: #labelCounts[key]=|c1 or c2|   numEntries=|D|
        prob = float(labelCounts[key]) / numEntries  # 9/14
        shannonEnt -= prob * log(prob, 2)
        # print(labelCounts[key])
    return shannonEnt


def SplitData(dataSet, axis, value):
    # 创建返回的数据集列表
    retDataSet = []
    # 遍历数据集
    dataSet_copy=copy.copy(dataSet)
    for featVec in dataSet_copy:
        if featVec[axis] == value:

            # 去掉axis特征

            # retDataSet.append(featVec.remove(value))

            # reduceFeatVec = featVec[:axis]
            #
            # 将符合条件的添加到返回的数据集
            reduceFeatVec=(featVec[:axis])
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)

    # 返回划分后的数据集

    return retDataSet

def ChoosebestSplitData(data):

    numFeatures = len(data[0]) - 1
    baseEntropy = calcShannonEnt(data)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in  data]
        uniqueVals = set(featList)
        newEntropy = 0.0

        for value in uniqueVals:
            subDataSet = SplitData(data, i, value)  # 逐个划分数据集，得到基于特征i和对应的取值划分后的子集
            prob = len(subDataSet) / float(len(data))  # 根据特征i可能取值划分出来的子集的概率
            newEntropy += prob * calcShannonEnt(subDataSet)  # 求解分支节点的信息熵
        infoGain = baseEntropy - newEntropy  # 计算信息增益
        if (infoGain > bestInfoGain):  # 对循环求得的信息增益进行大小比较
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] =0
        classCount[vote] +=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


#创建树
def createTree(dataSet, labels):
    # 取分类标签（是否出去玩：yes or no）
    classList = [example[-1] for example in dataSet]
    # 如果类别完全相同则停止继续划分
    if classList.count(classList[0]) == len(classList):    #判断一个列表里的标签是否一样
        return classList[0]
    # 遍历完所有特征时返回出现次数最多的类标签
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    # 选择最优特征
    bestFeat = ChoosebestSplitData(dataSet)
    # 最优特征的标签
    bestFeatLabel = labels[bestFeat]
    # featLabels.append(bestFeatLabel)
    # 根据最优特征的标签生成树
    myTree = {bestFeatLabel: {}}
    # 删除已经使用的特征标签
    # 得到训练集中所有最优解特征的属性值
    featValues = [example[bestFeat] for example in dataSet]
    # 去掉重复的属性值
    uniqueVals = set(featValues)
    # 遍历特征，创建决策树
    for value in uniqueVals:
        del_bestFeat = bestFeat
        del_labels = labels[bestFeat]
        del (labels[bestFeat])
        myTree[bestFeatLabel][value] = createTree(SplitData(dataSet, bestFeat, value), labels)
        labels.insert(del_bestFeat, del_labels)
    return myTree






if __name__=="__main__":
    date,lable = create_date()
    featLabels=[]
    print(createTree(date,lable))
    my_three=createTree(date, lable)


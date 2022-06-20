# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/23 11:31
@Auth ： victory.He
@File ：Pandas.py
@IDE ：PyCharm
@Motto：(Always Be Coding)
@Function：
"""
import pandas as pd
import csv
name=["Avery Bradley",'Jae Crowder',"John Holland","Jonas Jerebko"]
age=[18,12,46,53]
city=["Beijing","shanghai","shenzheng","guanggong"]
sex=["male","male","male","male"]     # male    female
data={"name":name,"age":age,"city":city,"sex":sex}
user=pd.DataFrame(data)
(user["sex"])[2]="female"
user.to_csv('user.csv')
class_user=[1,1,1,1]
user["class"]=class_user

#方法二 user.insert(4,"class",class_user)


# print(user)
#方法三
# class_student=[date,"class":class_user]
# with open("user.csv","wb") as f:
#     file=csv.writer(f)
#     file.writerows(class_student)


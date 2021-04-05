# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 作业.py
@date: 2021/01/23 18:42
"""

"""
1、定义函数：（要求：定义函数处理逻辑。考虑参数哦！！）
将输入的所有数字相乘之后对20取余数
用户输入的数字个数不确定

2、列表去重
定义一个函数 def remove_element(m_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素

4、编写如下程序（要求：定义函数处理逻辑。考虑参数哦）
尝试函数封装：

输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数

a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8

b.根据BMI指数，给与相应提醒

低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖



"""
#1、定义函数：（要求：定义函数处理逻辑。考虑参数哦！！）
#将输入的所有数字相乘之后对20取余数
#用户输入的数字个数不确定


"""
def deal(*args):
    sum = 1
    for item in args:
        sum *= item
    left = sum % 20
    print("对20取余结果为: {}".format(left))

# deal(2)
# deal(10)
# deal(1, 3, 5, 6, 22)
# deal()


nums = input("请输入数字(用逗号隔开每一个数字)")
# nums = [20,  30, 40]
new_list = []
for item in nums.split(","):
    new_list.append(int(item))
print(new_list)

"""


#第二题
#定义一个函数 def remove_element(m_list):，
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
my_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
newlist = []
for item in my_list:
    if item not in newlist:
        newlist.append(item)
print(newlist)






"""
my_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]


def remove_element(my_list):    # 定义函数
    print(list(set(my_list)))     # 现将列表转换成集合，在将几回合转换成列表


remove_element(my_list)    #  调用函数



"""

#第三题


"""计算bmi, 根据身高和体重
身高（单位m)
体重（单位kg)
18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
"""
def get_bmi(height,weight):
    bmi = weight / height ** 2
    if bmi < 18.5:
        print("太轻了")
    elif 18.5 < bmi < 25:
        print("正常")
    elif 25 < bmi < 28:
        print("肥胖")
    else:
        print("太胖")


h = 1.77
w = 54
res = get_bmi(h,w)






# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 作业.py
@date: 2021/01/14 22:30
"""
"""
1、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
（提示：通过字符串分割，拼接，列表反序等知识点来实现）


2、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
        1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
        2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
        3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 
        4、平台为了保护你的隐私，需要你删除你的联系方式；
        5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。

3、利用下划线将列表li=["python","java","php"]的元素拼接成一个字符串，然后将所有字母转换为大写，

4、有下面几个数据 ，
t1 = ("aa",11)      t2= ("bb",22)    li1 = [("cc",11)]
请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":11,"bb":22}(ps: 元组取值，然后给字典添加key-value)




"""
"""
#1、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
#（提示：通过字符串分割，拼接，列表反序等知识点来实现）

new_list = ["hello",  "xiao", "mi"]
new_list_new = new_list[::-1]
print("原始列表:", new_list)
print(new_list_new)
"""

"""
#2、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
#        1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
#        2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
#        3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
#        4、平台为了保护你的隐私，需要你删除你的联系方式；
#        5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
name = input("请输入姓名")
sex = input("请输入您的性别")
age = input("请输入宁的年龄")
dic = {}
dic.update({"name": name, "sex": sex, "age": age})
print(dic)
print("我的名字{}，性别{}，今年{}岁，喜欢敲代码".format(dic["name"], dic["sex"], dic["age"]))
high = input("请输入您的身高")
phone = input("请输入您的联系方式")
dic.update({"high": high, "phone": phone})
print(dic)
del dic["phone"]
print(dic)
dic["happe"] = ["打游戏"]
print(dic)

"""

#3、利用下划线将列表li=["python","java","php"]的元素拼接成一个字符串，然后将所有字母转换为大写，

"""
li = ["python", "java", "php"]
a = li[0]
for i in li[1:]:
    a += "_" + i
print(a)
print(a.upper())
"""

#有下面几个数据 ，
#t1 = ("aa",11)      t2= ("bb",22)    li1 = [("cc",11)]
#请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":11,"bb":22}(ps: 元组取值，然后给字典添加key-value)

t1 = ("aa",11)
t2 = ("bb",22)
t3 = [("cc",11)]

new_1 = {}
new_1[t1[0]] = t1[1]
print(t3[0])


"""
t1,t2,t3 = ((“aa”,11),(‘bb’,22),[(“cc”,11)])
list_1 = [t1[0],t2[0],t3[0][0]]
list_2 = [t1[1],t2[1],t3[0][1]]
new_dict_1 = {}
for i in range (3):
    new_dict_1[list_1[i]] = list_2[i]
"""












# -*- coding:utf-8 -*-
"""
@author:luomi
@file: for循环.py
@date: 2021/01/16 17:32
"""
"""
for 循环 - for遍历  - 列表/字典/元组/字符串都可以遍历

班级 - 列表 - 成员
老师遍历这个列表,与每个成员打个招呼

遍历:从头到尾访问一遍

语法:

for 变量名 in 列表/字典/元组/字符串:
    渠道每一个成员后,会执行的代码(会做的事情)

for后面的变量名,取出来的每一个值都会用变量名去接受

break:退出循环

continue:跳过本轮循环,不执行continue之后的代码,直接进入下一轮循环

for循环:遍历次数是:列表/字典/元组/字符串的长度

遍历次数- 固定/不固定  -不固定选择while/固定选择for

避免死循环- 循环条件的变更

列表和字典的遍历:
    1.遍历列表的值(成员)
    2.遍历列表的下标,通过下标去取值
    
生成整数列表的方法: range
range(起始整数,结束整数,步长)  起始整数默认为0,步长默认为1,左闭右开(取头不取尾)
range(5) => [0,1,2,3,4]
range(1,5) => [1,2,3,4]
range(1,10,随意输入数字) => [1,3,4,6,9]


字典的遍历:
字典的成员 key value


"""
# 1.列表遍历 - 遍历列表的值
#new = ["小李子","小豆子","小楠楠","明明","天天","小李子"]

"""
for item in new:
    print(item)
    
for item in new:
    print(f"你好呀,{item}")
    if item == "小楠楠":
        break
        
"""
"""

for item in new:
    if item == "小楠楠":
        continue
    print(f"你好呀,{item}")
    
"""
"""
for item in new:
    print(f"你好呀,{item}")
    if item == "小楠楠":
        continue

"""
"""
# 2.遍历列表的下标,通过下标去取值
new = ["小李子","小豆子","小楠楠","明明","天天","小李子"]

for item in new:
    print(f"你好呀,{item}")
    if item == "小楠楠":
        continue

for index in range(len(new)):
    #print(index) # 索引
    #print(new[index]) # 索引对应的值
    print("索引为{}的值是:{}".format(index,new[index]))
"""

# 字典遍历

person_info = {"name": "X", "age": "19", "city": "上海", "girl":""}

for key in person_info.keys():
    print(key)


for item in person_info.items():
    print(item)
# 和第1一样的意思
for key,value in person_info.items():
    print(key)

for key,value in person_info.items():
    print(f"{key}:{value}")

"""
# 计算1-100的和
#sun = 1 +2 +3 +5 - 100
# 怎么样去生成一个1,2,3,4,,,100的列表

sum = 0
for a in range(1,101):
    print(a)
    sum += a
print("sum为:",sum)

"""










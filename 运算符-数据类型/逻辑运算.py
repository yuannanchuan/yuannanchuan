# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 逻辑运算.py
@date: 2021/01/09 12:02
"""


" and与  or或 not非 逻辑结果为:布尔值 左边右边的条件都是True False "

#input:运行代码的时候接受用户的输入.
#变量接受到的用户输入值,均为字符串
salary = input("请输入你的目标")
print(salary)

# type(变量) - 获取变量的数据类型
#print(type(salary))

# ==同数据类型的比较,最好转换为同一个数据类型,再去比较
# 数字内容的字符串,转成int/float类型. -- int(salary)
#res = int(salary) == 18000
#print(res)

#res = (int(salary) == 20000) and (addition == "双休")
#print(res)

res = (int(salary) == 20000) or (addition == "双休")
print(res)


#print(not int(salary) > )



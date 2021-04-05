# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 字符串操作.py
@date: 2021/01/09 16:32
"""

"""
#index(索引/下标)
#  --index(子字符串).返回它的下标,如果找不到就会抛异常,ValueEorror:substring not found

格式化输
    字符串里边有一部分是动态的
    {}占位符
    替换占位符的时候,可以是任意类型
    format函数:字符串,format(第一个值,第二个值,第三个值)
            下标位置是:        1       2      3


py.3.7版本之后的:f表达式            
     {}占位符
     替换被占位符的时候,可以是任意类型
     f"{表达式}"       


"""
by_hobby="Never stop learnoing"
#print(by_hobby.index("w"))#会报错

print("-------------")
print(by_hobby.find("w"))

#字符串里边有一部分是动态变化的
age = input("请输入您的年龄")
heifht = 18

#一个萝卜一个坑,每个萝卜填每一个坑

#print("猜猜我的年龄多少:{}","身高是:{}cm".format(age,height))
#print("{} {} = {}".format(8,8,8*8))

#一个萝卜要填在几个坑里面(占位符填入下标)
#print("{0} * {0} = {1}".format(8,8*8))

#再字符串里面显示小数点.{:.2}表示显示小数点2位
#print("{} * {} = {:.2}".format_map(1.12,3.33,4.44,2,21*6.65))

#在字符串里面显示百分比
#print("今天能够吃几顿饭:{:.%}".format_map(0.23455))

#   f表达式
#print("{} * {} = {}".format_map(8,8,8*8))
#num1 = 100.111
#num2 = 200.23
#print(f"{8} * {8} = {8*8}")
#res = num1 * num2
#print(f"{num1} * {num2} = {res:.2f}")
print(f"今天休息天吗??{100 == 100}")





# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 作业代码.py
@date: 2021/01/23 20:29
"""

"""
1，  使用for打印九九乘法表
提示：
输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

1 * 1 = 1	
1 * 2 = 2    2 * 2 = 4	
1 * 3 = 3    2 * 3 = 6      3 * 3 = 9	
1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16	
1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25	
1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36	
1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49	
1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64	
1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81

2、使用函数封装。定义函数，并通过给函数传递不同的参数(要想清楚哪些做为参数哦！！)：
1、一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买
金额50-100元(包含50元和100元)之间，会给10%的折扣，
如果购买金额大于100元会给20%折扣。编写一程序，询问购买价，再显示出折扣（%10或
20%）和最终价格。
"""
def pay_money(price):
    if type(price) == float:
        if 50 <= price <= 100:
            discount = 0.1
        elif price > 100:
            discount = 0.2
        else:
            discount = 0
        pay = (1 - discount) * price
        print("我的折扣是: {}".format(discount))
        print("我最终要付的价格是:{:.2f}".format(pay))


price = input("请输入价格: ")
pay_money(float(price))

pay_money(300)

"""

3、冒泡排序（不要求提交，面试之前背熟）
使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）
提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
编码提示：

1、先写出第一轮比较的代码哦。如在a当中，将最大的一个数据放在列表最后。

2、再写出第二轮比较的代码：在1之后的列表当中，将第二大的数据，放在列表的倒数第二

3、以此类推

4、比对以上所写的代码，有何相同，有何不同之处。再考虑使用外层for来替换

"""
"""
#1
for a in range(1, 10):
    for j in range(1, a + 1):
        print(f" {j} * {a} = {j * a} ", end=" ")
        #print('%d*%d=%2d\t' % (j, a, a * j), end="")
    print()

"""

"""
# 第二题

#函数:实现一个功能,重复使用
#    -- 是否有参数 - 看使用这个功能的时候,有什么变化的


def pay_money(price):
    if type(price) == float:
        if 50 <= price <= 100:
            discount = 0.1
        elif price > 100:
            discount = 0.2
        else:
            discount = 0
        pay = (1 - discount) * price
        print("我的折扣是: {}".format(discount))
        print("我最终要付的价格是: {:.2f}".format(pay))


price = input("请输入价格:")
pay_money(float(price))

#pay_money(300)
#pay_money(80.8)
#pay_money(1000)

"""

"""
# 第三题
#冒泡排序（不要求提交，面试之前背熟）
#使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）
#提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
#编码提示：

m_list = [2, 90, 6, 3, 10, 48, 1, 33]


for a in range(1,len(m_list)):
    #print(a)
    for i in range(0, len(m_list)-a):
        #print(i)
        if m_list[i] > m_list[i+1]:
            m_list[i], m_list[i+1] = m_list[i+1], m_list[i]
print(m_list)
"""









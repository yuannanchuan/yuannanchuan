



"""

1. 异常捕获的语法是什么样的？    请列举你遇到过的/见过的错误类型。

"""
# try:
#     print("可能有异常的代码")
# except:
#     print("可能有异常代码后面的代码")
# else:
#     # try里的代码没出现异常，则执行此处代码
# finally:
#     # 无论try里的代码有没有出异常，必定会执行的操作。
#     # 一般来讲，清理工作。

# ImportError 导入错误
# SyntaxError 语法错误
# OSError路径错误
# AssertionError 断言报错
# AttributeError  属性报错
# KeyError  找不到key
# FileNotFoundError  找不到文件



"""
2.编写如下程序
优化去生鲜超市买橘子程序

a.收银员输入橘子的价格，单位：元／斤

b.收银员输入用户购买橘子的重量，单位：斤

c.计算并且 输出 付款金额

新需求：

d.使用捕获异常的方式，来处理用户输入无效数据的情况

"""

try:
    unit_price = int(input("输入橘子的价格："))
    weight = int(input("请输入橘子的重量："))
    sum = unit_price * weight

except:
     print("有无效数据")

else:
     print(sum)




"""



3、笔记总结哦



4、下节预告：类和对象




"""

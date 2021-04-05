# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 循环.py
@date: 2021/01/16 17:13
"""
"""
循环 - 上班-下班

while
while 条件:
      条件为真会执行的代码
      直到有一个条件不满足
            退出循环(break)
while的特点:
           有条件决定循环次数
           当我们的应用场景不确定循环次数的时候使用while   
            
死循环: 写代码的时候 一定要避免死循环
    第一种:再while内部,使用while的条件发生改变
    第二种:使用break    
  
for



"""

# while  使用例子
#while True:
#     print("66666666") # 死循环

"""
score = 88
while score >= 80:
     print("很棒棒哒")
     score -= 1  #再while运行的过程中,改变了条件中的数据/变量,总有一次让while的条件不成立
     if score == 86:
         break # 直接退出while循环


"""

score = int(input("请输入一个数字:"))
while score >= 80:
     print("很棒棒哒")
     score -= 1  #再while运行的过程中,改变了条件中的数据/变量,总有一次让while的条件不成立
     if score == 86:
         break # 直接退出while循环












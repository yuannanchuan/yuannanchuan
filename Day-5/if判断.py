# -*- coding:utf-8 -*-
"""
@author:luomi
@file: if判断.py
@date: 2021/01/16 16:45
"""
"""
if 条件1:
    条件1为真的条件下执行的代码(会干的事情)
elif 条件2
     条件2为真的情况下执行的代码(会干的事情)
else:
    条件1和2都不为真的情况下执行的代码(会干的事情)


"""
"""
score = input("请输入考试分数:")
if int(score) == 100:
    print("非常棒棒哒")
    print("很流批")


print("**************")

if int(score) == 100:
    print("非常棒棒哒")
    print("你很棒棒哒")
elif 80 <= int(score) < 100:
    print("要努力学习了")
elif 70 <= int(score) < 100:
    print("再不努力要挨打了哟")
else:
    print("竹笋炒肉来一发")

"""
#输入一个周一到周天,双休
#根据输入的内容来判断要上还是不要上班
#周一到周五上班  周六周天不上班

working_day = ["星期一","星期二","星期三","星期四","星期五"]
weekend = ["星期六","星期天"]

value = input("请输入周一到周天:")
if value in working_day:
    print("要出发取搬砖哟,请勿偷懒!!!")
elif value in weekend:
    print("可以睡懒觉的周末很爽呀")
else:
    print("请输入正确的数据-星期一到星期天")







# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 函数的参数.py
@date: 2021/01/23 21:59
"""
"""

def 函数名(参数1, 参数2, 参数3)

2.调用函数的时候,传递的是实参.

参数第1种形式:位置/必传参数 可以有多个.传参时  --对应

参数第2种形式:默认参数 - 默认值
            定义函数的时候,形参=默认值
            关键字参数
参数的第3种形式:不定义参数
              *args
              **kwargs
              

返回值

 传参时: key=value
"""


desc_your_feather(name="不知道", age=29, sex="gir")




def both(*args, **kwargs):
    print("打印单身狗agrs:{}".format(args))
    print("打印非单身狗及其对象信息kwargs:{}".format(kwargs))


both("y圆圆","陈独秀","人生啊","爱情啊",so="soso",yijiu="leisen")























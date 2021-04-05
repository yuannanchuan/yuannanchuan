# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 字符串join和split.py
@date: 2021/01/14 22:09
"""
"""
与列表相关:
join : 拼接符.把字符串列表里的每一个成员,用;拼接成一个字符串
split : 分割,分隔符.把一个字符串,按照分割符,切割成多个子字符串,分割完成之后是一个列表
列表一般来讲,存放的数据,都是同一类型
"""
xinxi = "名字:囡囡 年龄:18 性别:女 地区:上海"

# 字符串.split(分割符) #分割符不传,默认是根据空格来切割字符串,切割之后,列表的成员一定是字符串

res = xinxi.split(",")
print(res)
#res = xinxi.split(" ")
#print(res)

#字符串列表里的每一个成员,用;拼接成一个字符串
# 拼接符.join(列表)
# 注意:列表当中的每一个成员都必须是字符串,否则会报类型错误:TypError
#list1 = ['名字:囡囡', '年龄:18', '性别:女', '地区:上海',True]
#new_res = ";".join(list1)
#print(new_res)

list1 = ['名字:囡囡', '年龄:18', '性别:女', '地区:上海']
new_res = ";;".join(list1)
print(new_res)










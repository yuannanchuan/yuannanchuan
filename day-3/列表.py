# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 列表.py
@date: 2021/01/09 17:18
"""
"""
字符串:str
列表:list []

"""

#空列表
list_empty = []


#非空列表. 成员.每个成员之间用逗号隔开
#成员可以是任意类型
#可以重复
#列表是有序的,可以通过索引取值
list_py37 = ["小李子","小豆子","小楠楠","明明","天天","小李子"]
py37_teacher = ["简神"]
py37_listsss = [111,222,[6666,7777]]

#取值. - 下标取值.列表名[下标] 下标从0开始
#注意下标不能越界
print(list_py37[2])

#获取某一个成员的下标 - 列表名.index(成员)
index = list_py37.index("小楠楠")
print(index)

#支持切片,列表名[开始索引(默认为0):结束索引:步长(默认为1)]
print(list_py37[:4])
#列表反转
print(list_py37[::-1])


#往列表里面:添加值
#1.append(新的值) - 往列表末尾添加值
list_py37.append("小墩子")
print(list_py37)


#list_empty = []   #空列表
#list_empty[0] = "鸡肉卷"
#print(list_empty)
#list_empty.append("牛肉卷")
#print(list_empty)

#  insert(下标,新的值)  - 再某个位置插入某个值
list_py37.insert(0,"小胖子")
print(list_py37)

#   extend(新列表)   -  合并2个列表
#new_list = ["鸡肉卷","牛肉卷","猪肉卷","排骨卷","蛋白卷"]
#list_py37.extend(new_list)
#print(list_py37)

#  修改列表当中的值  修改索引对应的值.
#  列表[索引] = 新的值
list_py37[1] = "小囡囡"
print(list_py37)

#  删除操作  - 从列表中删掉某个成员
#  通过值来删除  - remove
list_py37.remove("小墩子")   #查看源码 ctrl+B
print(list_py37)
#  通过下标来删除
del list_py37[0]
print(list_py37)

#  列表名.pop() 删除列表的最后一个
list_py37.pop()
print(list_py37)

#列表名.pop(index)  删除指定下标对应的值
list_py37.pop(1)
print(list_py37)
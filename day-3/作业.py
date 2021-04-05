# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 作业.py
@date: 2021/01/09 18:31
"""
"""
现在有一个列表 li2=[1，2，3，4，5]，
请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，

"""
#li2 = [1,2,3,4,5]
#li2.insert(0,0)
#print(li2)
#li2.insert(4,66)
#print(li2)
#new_li2 = ["11","22","33"]
#li2.extend(new_li2)
#print(li2)


"""
4、有4道小题（使用列表操作完成）：
a.  某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
c, 平台为了保护你的隐私，需要你删除你的联系方式；
d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
e, 你进一步添加自己的兴趣，兴趣至少包含 3个(注意：兴趣是另外一个列表。请将这个列表作为一个成员，添加到原个人信息列表当中，添加到末尾即可。)。

"""
list_yqq = ["袁女士","女","18"]
print(list_yqq)

list_yqq.append(155,)
print(list_yqq)

list_yqq.append(15566666666)
print(list_yqq)

list_yqq.remove(15566666666)
print(list_yqq)
#二选一
#del list_yqq[3]s
#print(list_yqq)

list_yqq[0] = "囡囡"
print(list_yqq)

list_yqq[3] = "177"
print(list_yqq)

new_list = ["看书","刺绣","手工活"]
list_yqq.extend(new_list)
print(list_yqq)








# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 列表操作.py
@date: 2021/01/14 21:37
"""
"""



"""
new_list = ["花花", "曹操", "小鸡", "兔子", "小鸭子", "白白"]
#列表的长度 - len()

print(len(new_list))

#列表成员运算符 - 是否是成员之一
#成员 in 列表   成员  not in  列表   结果为True,False

# print("拜拜" in new_list)
# print("白白" in new_list)


#排序和反转
# 排序 - 降序,升序
# 1.列表.sort() 默认为升序
# print(new_list)
# new_list.sort()
# print("升序排序之后的:", new_list)#对原列表进行了修改

# list2 = [100, 99, 88, 77, 22, 44, 65, 32]
# list2.sort()
# print("排序之后的:", list2)
# list2.sort(reverse=True) #降序排序
# print("降序排序之后的:", list2) # 对原列表进行了修改


# 2.python自带的sorted(列表) - 排序
# changed_list = sorted(list2)
# print("sorted排序之后,原始列表:", list2)
# print("sorted排序之后,生成新的列表:", changed_list)
# changed_list2 = sorted(list2, reverse=True) # 降序排序


# 列表反转
# 1.切片 列表名[::-1] - 新生成列表
new_list_new = new_list[::-1]
print("原始列表:", new_list)
print(new_list_new)

# 2.列表.reverse() - 对原列表进行了反转操作
new_list.reverse()
print("调用reverse方法之后的源列表为:", new_list)


# 总结: 列表.XXX() - 如果是修改操作,一般是对原始列表进行修改

# 获取成员出现的次数
new = new_list.count("白白")
print(new)





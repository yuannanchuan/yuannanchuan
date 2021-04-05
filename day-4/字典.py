# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 字典.py
@date: 2021/01/14 22:28
"""
"""
数据类型有:
        可变类型:list, dict
        不可变类型:int, float, str, tuple
 1.列表:[]  有序,有索引,值可以重复/任意类型
 2.字典:{}  键值对{key-value}  无序  key是唯一的且不可变的,一般都是字符串. value可以是任意类型
 3.元组: () 与列表一样,有序有索引,值可以重复(可以是任意类型,但是建议全部放不可变量类型)
           但是它是不可变类型,只可以读不可以对它进行修改.
           读取:根据索引读取,从0开始,元组[索引]
           获取长度:len(元组)
           在表达一个值的时候:(值1,)
"""

# 字典
empty_dict = {}
person_info = {"name": "X", "age": "19", "city": "上海", "girl":""}

# 查询 - 通过key取获取
# 1. 字典[key] 如果KEY不存在字典当中,就会报错:keyError
#print(person_info["age"])
#print(person_info["happe"]) # 不存在key报错:keyError

# 2.字典.get(key) 如果key不存在字典当中,则为Noen
#print(person_info.get("age"))
#print(person_info.get("happe"))

#  添加key-value,修改key对应的value
#  字典[key] = value
#  key如果存在字典就是修改,如果key不存在字典就是添加
person_info["name"] = "囡囡"  # 修改
print(person_info)
#person_info["happe"] = ["打游戏", "刺绣", "看综艺"] #添加
#print(person_info)
#person_info["ganxinqude"] = {"旅游": ["大理","云南"]}
#print(person_info)
"""
# 主要是用新增值上面 sedefault - 设置默认值
#  字典.sedefault(key,默认的value)
person_info.setdefault("height", 165)
person_info.setdefault("name", "大囡囡")
print(person_info)

# 2个字典合并
# 字典1.update(新字典) 将新的字典合并到字典1当中
new_dict = {"sex": "girt", "weight": 90}
person_info.update(new_dict)
print(person_info)

# 删除操作 - del操作,pop操作也可以
del person_info["girl"]   # 删除主键key
print(person_info)

"""
"""
#  要获取所有的keys - 字典.keys()
print(person_info.keys())
#  要获取所有的value - 字典.value()
print(person_info.values())
#  要同时获取所哟的key和value - 字典.items()
print(person_info.items())
"""
"""
# 成员运算符
print("name" in person_info)
print("name" in person_info.keys())
print(19 in person_info.values())
print(('name', "X") in person_info.items())

#  获取长度
print(len(person_info))
"""





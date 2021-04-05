# -*- coding:utf-8 -*-
"""
@author:luomi
@file: 字符串.py
@date: 2021/01/09 12:20
"""

"""
str - 字符串

1.字符串表示 - 单双引号,三引号

2.字符串下标/索引取值
    取值:取指定位置
    索引/下标
    正向索引
    逆向索引
3.切片

"""


#str_empty = " "  # 空字符串
#print(str_empty)

#str_py37 = "yangrou,niurou py37 hello data"
#字符串变量名[下标] - 下标从0开始往后数
#当字符串下标越界时报错:IndexError:string index out of range
#print(str_py37[1])


#str1 = 'python cainiao 666'
#print(str1[5])


#字符串长度多少呢? len(字符串变量名)
#length = len(str_py37)
#print(length)

#去最后一个值
#print(str_py37[40])
#print(str_py37[length - 1])
#print(str_py37[-1])



str_py37 = "yangrou,niurou py37 hello data"
#切片.字符串变量名(起始下标:步长)  起始下标默认为0,步长默认为1
#左闭右开,取头不取尾(如果取前4位那么输入必须输入0:5才能够取到前四位想要的内容)
#步长为正,表示正序
#步长为负,表示倒叙
print(str_py37[0:4])  # 0,1,2,3
print(str_py37[0:5])  # 0,1,2,3,4
print(str_py37[:5])  # 0,1,2,3,4

#正着取
#print(str_py37[::])
#print(str_py37[::1])
#把字符串倒序输出
print(str_py37[::-1])

#  -2 -2-2=-4   -4-2=-6  -6-2=-8
#print(str_py37[-2:-8:-2])

# 2+2=4  4+2=6    6+2=8
#print(str_py37[2:8:2])

#print("#$$$$$$$$$$$$ 字符串操作 *******")
#不管用那个字符串操作,都不会对原始字符串做修改,重新生成个字符串
str_py37 = "hahahha PY37"
# 小写 大写
nuw_str_py37.lower()  #全部都转成小写
print(str_py37)

new = str_py37.upper() #全部都转成大写
print(new_str)

#查找和替换,字符串变量.find(子字符串)
#如股票找到了.返回的时起始下标
#如果没找到,返回的是-1
res = str_py37.find("37")
print(res)

res = str_py37.find("444")
print(res)

res = str_py37.find("37",7)
print(res)

#替换    字符串变量.replace(新的,旧的)   匹配到的所有的都会替换
#       字符串变量.replace(旧的,新的,替换的次数[可选])   只替换指定的次数的
str_2 = "hello,py37,nmb"
new_str = str_2.replace("hello","666")
print(new_str)

#new_str = str_2.replace("hello","666",1)
#print(new_str)

#替换的值,只能是字符串
#否者会报错: TypError::replace() argument 2 must be str, not int
#new_str = str_2.replace("hello",666,1)
#print(new_str)

new_str = str_2.replace("hello","哎呀,不好意思啊",1)
print(new_str)


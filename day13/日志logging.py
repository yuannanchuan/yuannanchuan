

"""
print/断点 - 本地调试


日志: 记录了执行过程 - 逻辑执行流程
     记录了报错 -

1.在代码里写,添加日志代码 - 在那些地方你先输出日志. info-error-debug
2.收集代码当中的日志信息,然后输出

logging模块:


1.日志收集器
    定义日志收集器: 要从代码当中按照要求 收集对应的日志,并输出到渠道当中.
        1)要收集那个级别以上的日志?
        2)日志是要什么样的格式显示
        3)日志压迫输出到那些地方去

2.日志级别(level):
        debug - info - warning - error - critical(FATA)
         调试    基本     警告      报错      严重错误

3. 日志显示的格式:
    时间,日志级别,代码文件,第几行:信息

4.日志输出渠道(handle)
    文件(.log)
    文件(FileHandle),控制台(StreamHandle)

logging模块: 有一个默认的日志收集器,root
    a.手机的是warning及warning级别以上的日志
    b.日志格式:日志级别:收集器名字:输出的内容
    c.输出渠道:控制台

自动逸日志收集:
1.调用logger = logging.getLogger(日志名字)来生成一个日志收集器对象
2.设置你的日志收集器级别. logger.setLevel(日志级别) 一般为INFO
3.使用logging.Formatter类来定制要输出到控制台/文件当中的日志格式
4.使用handele1 = logging.StreamHandle()来创建一个控制台渠道对象
5.将4当中的handle1添加到logger当中,那么日志就可以输出到控制台.

6.使用handle2 = logging.FileHandle(日志文件路径)来创建一个控制台渠道对象
  并将控制台要输出的日志格式设置为3当中的formatter. 设置:handle2.setformatter(Formatter)
7.将6当中的handle2台南佳到logger当中,那么日志就可以输出到文件当中.

6.使用handle3 = logging.FileHandle(日志文件路径)来创建一个控制台渠道对象
  并将控制台要输出的日志格式设置为3当中的formatter. 设置:handle2.setformatter(Formatter)
  指定handle3的日志级别为ERROR
7.将6当中的handle3添加到logger当中,那么日志就可以输出到文件当中.


"""

import logging



class Student:

    identify = "Student"

    def __init__(self,name,age,sex,cn_score,math_score,en_score):
        self.name = name
        self.age = age
        self.sex = sex
        self.cn_score = cn_score
        self.math_score = math_score
        self.en_score = en_score
        logging.info("hello,logging????")

    def get_sum_of_score(self):
        sum = self.cn_score + self.math_score + self.en_score
        logging.critical("{} 的语数外总分为: {}".format(self.name, sum))
        return sum

    def get_avg_of_score(self):
        avg = self.get_sum_of_score()/3
        logging.error("{} 的语数外平均分为: {}".format(self.name, avg))

    def print_stu_info(self):
        logging.warning("我的名字叫: {},年龄: {},性别: {} ".format(self.name, self.age, self.sex))


bing = Student("圆圈圈",29, "男", 90, 80, 99)
bing.get_sum_of_score()
bing.get_avg_of_score()
bing.print_stu_info()









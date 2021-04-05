
"""

2021-0129 - 类和对象(2)
1， 详细总结类和对象知识点，包括：

类的定义
    方法 属性  类型  class关键字
对象的初始化
    __init__
类属性
    cls.
实例属性
self.XXX(类定义中) 或者对象.XXX
实例方法
实例方法:self   对象调用
类方法
类方法:cls  #classmethod
静态方法
  @statincmethod
        def 函数名称():
            函数实现
继承
    class 字类(父类1, 父类2)
        pass
重写

super 函数

2， 定义一个类 Dog, 包含 2 个属性：名字和年龄。
定义一个方法 eat 吃东西。
定义一个类 TeddyDog, 继承 Dog 类， Teddy 在吃东西的时候还会望着你，  定义方法 watch_you.
定义一个类 BabyTeddyDog, 继承 TeddyDog,  BabyTeddy 吃东西不仅会望着你，还会四处转悠， 定义方法 go_around
"""

"""
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃")


class TeddyDog(Dog):

    def watch_you(self):
        self.eat()
        print("看着你")


class BabyTeddyDog(TeddyDog):

    def go_around(self):
        self.watch_you()
        print("四处转悠")
"""


"""
二、选作题（不需要提交)
1.编写如下程序
编写一个工具箱类和工具类
工具类：需要有工具具的名称、功能描述、价格。
工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
工具比如锤子、斧头、螺丝刀等工具。
提示：不需要用到继承。

"""




class Tool:

    def __init__(self,name, price, func_desc):
        self.name = name
        self.price = price
        self.func_desc = func_desc

    def print_tool_info(self):
        print(f"工具名称: {self.name}\n工具价格: {self.price}\n工具的功能:{self.func_desc}\n")


class ToolBox:

    def __init__(self):
        self.tools = []  # 工具对象

    def add_tool(self, tool_obj):  # Tool类的对象作为方法的参数
        if tool_obj not in self.tools:
            self.tools.append(tool_obj)
        else:
            print("工具箱里已有")

    def del_tool(self,tool_obj):
        if tool_obj in self.tools:
            self.tools.remove(tool_obj)
        else:
            print("工具箱里无此工具")

     #  函数的参数   变量名: 数据类型/类    给形参一个注释,表示期望传入的类型,但是调用的收可以传别的类型
    def get_tool(self, tool_obj: Tool):
        if tool_obj in self.tools:
            tool_obj.print_tool_info()

    def get_count_of_tools(self):
        count = len(self.tools)
        print("工具个数为: {}".format(count))


tool1 = Tool("锤子", 20, "锤钉子")
tool2 = Tool("螺丝刀", 30, "拧螺丝")
tool3 = Tool("刨子", 40, "刨树皮")

#  实例化一个工具箱
gjx = ToolBox()

# 添加一个工具
gjx.add_tool(tool1)
gjx.add_tool(tool2)
gjx.add_tool(tool3)
gjx.get_count_of_tools()
gjx.get_tool(tool2)


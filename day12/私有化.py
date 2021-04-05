


"""

私有化 : 我想藏起来,不给外人看机胺/访问/修改

对象,钱财,伺私房钱,--隐私性很强

python棉面向对象 - 私房钱
        1._属性/_方法
            约定俗成.
            通过对象名._属性/_方法  实际上是可以访问的,
            但是它的意思是,别放问我,我是私有化,全靠自觉

        2.__属性/__方法
            深度私有.不可以访问()
            通过对象名.__属性/__方法访问不到
            之后类内可以访问

_和__私有化方式同样在模块(.py)当中也支持
模块内私有.仅想在模块内使用.其它模块到的时候,表示这些不想被外访问.


什么场景下使用
    -- 什么情况下定义的属性或者函数不需要被外部使用
    当模块/类要实现过一个大功能.二这个共功能由很多个内部的小功能(函数不应该太复杂)组成的.
    但是这些小功能对于使用者而言不需要看机胺/不需要使用,我们就会做成私有化.


自行拓展:__all__
"""

_hello = "world"

def __hello():
    print("我不想其它的模块访问")


# 抽象描述 -  定义
class Person:

    __flag = True

    def __init__(self, name, sex, city, age=18):
        self.my_name = name    # 给对象添加name属性,并给它赋值.
        self.my_sex = sex
        self.my_city = city
        self.my_age = age
        self.color = "中国人"  # 对象的color属性
        self._private_money = 2000
        self.__spri_money = 4000

    # 如果类内补定义了访问私有的方法,可以通过这个方法得到私有属性的值
    # 如果没有定义的话,那私有属性就是除了类以外.都不可以访问
    def get_spri_money(self):
        print(self.__spri_money)

    def updata_color(self):
        self.color = "中国汉族"
        print("对象的color为:{}".format(self.color))


pp = Person("哎呀妈呀", "男", "上海")
print("浅度私有: {}".format(pp._private_money))
#print("深度私有: {}".format(pp.__spri_money))



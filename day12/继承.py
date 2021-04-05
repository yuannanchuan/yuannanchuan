
"""
继承: 字类继承父类
    可以继承:财产,钱,人脉,资源
    不可以继承:媳妇/私房钱/....私有化

    _属性/_方法: 字类可以继承
    __属性/__方法: 字类不可以继承

python多继承: -- 继承多个父类 --
继承的语法:
    class 字类(父类1, 父类2)
        pass

字类继承父类,拥有父类所有属性和方法,除了私有化的以外

继承会面临2个问题:
1.你想在父类的功能或者属性以外,添加属于你自己嗯点特色的方法/属性.

2.字类和父类有同名方法 - 子类重写父类方法
    你想在父类的原有功能的基础上,去优化它/改变它
    即,你和父类和同名方法
    2.1 不动父类的共鞥,只是增加一些额外的功能
    2.2 推翻父类的功能,重新写一遍
 在与父类同名方法的类,想调用父类的同名方法,使用super


"""


class Father:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eare_money(self,work):
        print("{} 通过 {} 赚钱".format(self.name, work))

    def hobby(self, favirate):
        print("爸爸的爱好 {}".format(favirate))


class Son(Father):

    # 你想在父类的共鞥或者属性以外,添加属于自己特色的方法.
    def study(self,content):
        print("我通过学习 {} 来提成自己".format(content))

    def eare_money(self, work):
        # 在与父类同名方法的内,想调用父类的同名方法,使用super
        # super 超类
        super().eare_money(work)
        print("{}通过投资理财在赚了 2000块钱".format(self.name))  # 在父类的基础上,额外增加了

    # 完全自己重写
#   def eare_money(self, work1):
#        # 在与父类同名方法,但是我要完全重写,不用父类的代码
 #       print("{} 通过 {} 来赚钱".format(self.name, work1))



Mrm = Son("Mr圆", 20)
#Mrm.eare_money("做软件测试")
Mrm.eare_money("板砖")
#Mrm.hobby("赚钱")
#Mrm.study("和小件老师学习py自动化")
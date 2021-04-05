"""
类:抽象的,对象共有的特征
对象:有很多个,具体的存在


类(抽象描述)和对象(具体存在的)


python里面定义类(属性加功能): CLASS类名
python里面造对象: 实例化


class 类型(大驼峰命名):
      属性:名字, 性别, 国家, 年龄
      行为:吃喝拉撒, 是否有另一半, 学习, 下厨, 刺绣

对象余对象之间,没有任何关系
每个对象都是独立的

__init__ 方法:
    魔法 - 在创建对象的同时,自动调用,做初始化的动作.

实例属性(只有对象可以访问):self.XXX(类定义种) 或者 对象.XXX
类属性(类和实例都可以访问):类名.XXX

"""


# 抽象描述 -  定义
class Person:

    # 类属性 = 值
    color = "黄种人"

    def set_info(self, name, sex, city, age=18):
        self.my_name = name    # 给对象添加name属性,并给它赋值.
        self.my_sex = sex
        self.my_city = city
        self.my_age = age

    # 实列化对象的时候,对象是谁,self就是谁
    # 在定义类的时候,并不知道对象是谁,用self来表示对象.
    def eat(self, food=None):
        print("我喜欢吃{}".format(food))

    def study(self):
        pass

    def cooking(self):
        pass

    def find_another_friend(self, has_friend, food=None):
        """
        年龄 > 18,以及,没有对象的,就找对象,否侧就不找
        :param has_friend:  True或者False.True表示有对象.False表示没有对象
        :return:
        """
        if self.my_age >= 18 and has_friend is False:
            print("{} 需要找对象".format(self.my_name))
            # 告诉别人我喜欢什吃什么
            self.eat(food)
            # 不建议,动态添加的属性,只有在调用此方法才会有.其它情况下如何去引用就会报错

        else:
            print("没有资格找对象")

    def paly(self):
        pass

# 类名来访问类属性
print(Person.color)
print("=============")

# 类对象来访问类属性


"""
bql = Person("巧克力")
bql.find_another_friend(False,"冰淇淋")
"""

# 实例化类 - 创建对应的对象
# 对项目 = 类名()
#bql = Person()
# 对象名.方法名()
#bql.eat("巧克力")
#bql.set_info("巧克力", "女", "中国", 29)
#print(bql.my_name)

"""
# 对项目 = 类名()
圈圈 = Person()
# 对象名.方法名()
圈圈.eat("麻辣烫")
"""




"""

class Person:

    name = "圈圈"    # 类属性

    def __init__(self,name, sex, city, age=29):
        self.my_name = name  # 给对象添加name属性,并给它赋值.
        self.my_sex = sex
        self.my_city = city
        self.my_age = age


    # 实列化对象的时候,对象是谁,self就是谁
    # 在定义类的时候,并不知道对象是谁,用self来表示对象.
    def eat(self, food):
        self.cooking()
        print("我喜欢吃{}".format(food))

    def study(self):
        pass

    def cooking(self):
        pass

    def find_another_friend(self):
        pass

    def paly(self):
        pass

# 实例化类 - 创建对应的对象
# 对项目 = 类名()
bql = Person("巧克力", "女", "中国")
# 对象名.方法名()
bql.eat("巧克力")


"""


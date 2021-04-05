"""
实例属性(只有对象可以访问):self.XXX(类定义中) 或者对象.XXX
类属性(类和实例都可以访问):类名.XX 或者 对象.XX

1.实例属性和类属性的优先级?同名会不会覆盖?.....
对于对象而言,自己有就先用自己的,自己没有,就用类的.

2.类属性修改? - - 类方法(所有实例的共性) 代表当前类
    @classmethod
    def 类方法名(cls)
        方法实现

    与实例方法的区别:
    实例方法:self   对象调用
     类方法:cls  #classmethod     类和对象都可以调用. 一般是类去调用
     静态放发: 没有self护着cls @staticmethod  类和对象都可以调用


3.静态方法  --
        普通函数   - 没有必定要传的,参数类或对象,只不过它是放在类里面.
        @statincmethod
        def 函数名称():
            函数实现


实例方法?实例方法之间互调用? --不要,会死调
类方法
静态放发



继承 - super - 重写


"""
import random


def get_weather(self):
    weather = ["晴天", "小雨", "暴雨", "大风", "大雪", "小风"]
    index = random.randint(0, len(weather) - 1)
    return weather[index]


# 抽象描述 -  定义
class Person(object):
    # 类属性 = 值
    color = "黄种人"  #常量

    @classmethod   # 装饰器的语法糖  - java叫注解
    def update_class_color(cls):
        cls.color = "全世界的人"
        print(f"类的color为:{cls.color}")

    def _info__(self, name, sex, city, age=18):
        self.my_name = name    # 给对象添加name属性,并给它赋值.
        self.my_sex = sex
        self.my_city = city
        self.my_age = age
        self.color = "中国人"  # 对象的color属性

    def updata_color(self):
        self.color = "中国汉族"
        print("对象的color为:{}".format(self.color))

    def play_something_by_weather(self):
        #  根据天气去判断玩什么
        taday_w = self.get_weather()
        pass

    @staticmethod
    def get_weather(self):
        weather = ["晴天", "小雨", "暴雨", "大风", "大雪", "小风"]
        index = random.randint(0, len(weather)-1)
        return weather[index]


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


# 类名来访问类属性
print(Person.color)
Person.updata_class_color()
print("=============")


# 对象来访问类属性
tz = Person("哈哈", "男", "上海")
print(tz.color)
tz.updata_color()
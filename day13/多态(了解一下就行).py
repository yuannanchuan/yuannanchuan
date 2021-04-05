


"""


"""


class People:
    def run(self):
        print("人类再跑")


class Dog(People):
    def run(self):
        print("狗在跑")


class Cat(People):
    def run(self):
        print("猫在跑")


mycat = Cat()
# 判断某一个对象,是否为类的一个实例
print(isinstance(mycat, Cat))
print(isinstance(mycat, People))

# 多态:父类类型 - 接受字类对象
# python没有多态, 处处皆多态 -- 鸭子类型(自行了解)


# python: 函数参数不做类型限制
def who_can_run(obj:People):
    obj.run()

mycat = Cat()
who_can_run(mycat)
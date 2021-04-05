



# 抽象描述 -  定义
class Person:

    def __init__(self, name, sex, city, age=18):
        self.my_name = name    # 给对象添加name属性,并给它赋值.
        self.my_sex = sex
        self.my_city = city
        self.my_age = age
        self.color = "中国人"  # 对象的color属性

    def updata_color(self):
        self.color = "中国汉族"
        print("对象的color为:{}".format(self.color))


qq = Person("圈圈", "女", "上海")


# 如果圈圈没有hobby这个属性,我就给他添加一个
if not hasattr(Person, "hobby"):
    setattr(Person,"hobby", "听歌")

print(Person.hobby)

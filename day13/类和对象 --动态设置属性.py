
"""
动态设置属性:
    在类定义之外,增加的属性,在代码的执行过程当中,动态添加的属性


hasattr(类/对象, 属性)  -  类/对象  是否有某个属性
setattr(类/对象, 属性, 值)  -  给类/对象  设置某个属性
gatattr(类/对象, 属性)  -  获取类/对象  某个属性
dalattr(类/对象, 属性)  -  删除类/对象  某个属性





"""

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

# 获取对象的hobby属性
#Value = getattr(qq,"hobby")
#print("之前", Value)

# 如果圈圈没有hobby这个属性,我就给他添加一个
if not hasattr(qq, "hobby"):
    setattr(qq,"hobby", "听歌")

#获取对象的hobby属性
Value = getattr(qq,"hobby")
print("之后: ", Value)

# 删除hobby属性
delattr(qq, "hobby")




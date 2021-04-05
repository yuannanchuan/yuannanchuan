
"""
2021 - 0127 - 类和对象1
1、实例属性怎么定义？
self.属性名 = 属性值

 2、实例方法中的self代表什么？（简答）
 代表对象

 3、类中__init__方法在什么时候会调用的？（简答）
实例化对象的时候调用

"""


"""
 5、封装一个学生类Student，(自行分辨定义为类属性还是实例属性，方法定义为实例方法) -
      - 属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
      - 方法一：计算总分，
      - 方法二：计算三科平均分
      - 方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx,性别：xxx。
请定义此类，并实例化1个学生,并打印学生个人信息，计算总分。

附加: 请根据学生的平均分,给评级,大于60分法1000 小于60分
"""


class Student:

    identify = "Student"

    def __init__(self,name,age,sex,cn_score,math_score,en_score):
        self.name = name
        self.age = age
        self.sex = sex
        self.cn_score = cn_score
        self.math_score = math_score
        self.en_score = en_score

    def get_sum_of_score(self):
        sum = self.cn_score + self.math_score + self.en_score
        print("{} 的语数外总分为: {}".format(self.name, sum))
        return sum

    def get_avg_of_score(self):
        avg = self.get_sum_of_score()/3
        print("{} 的语数外平均分为: {}".format(self.name, avg))

    def print_stu_info(self):
        print("我的名字叫: {},年龄: {},性别: {} ".format(self.name, self.age, self.sex))


bing = Student("圆圈圈",29, "女", 90, 80, 99)
bing.get_sum_of_score()
bing.get_avg_of_score()
bing.print_stu_info()


"""

第4题 ：定义类并实例化对象
定义一个登录的测试用例类LoginCase。每一个实例对象都是一个登陆测试用例。
 属性：用例名称 预期结果 实际结果(初始化时不确定值哦)
方法：
      1) 运行用例
         说明：有2个参数：用户名和密码。 能够登录成功的用户名：py37, 密码：666666。
         通过用户名和密码正确与否来判断，是否登录成功。并返回实际结果。
         ps: 可以在用例内部考虑处理不符合的情况哦：密码长度不是6位/密码不正确/用户名不正确等。。
      2) 获取用例比对结果(比对预期结果和实际结果是否相等，并输出成功or失败)

 实例化2个测试用例 ，并运行用例(调用方法) ，呈现用例结果(调用方法)
"""


class LoginCase:

    def __init__(self, case_name, case_expected):
        self.case_name = case_name
        self.case_expected = case_expected
        self.case_actual = None

    def run_case(self,user,passwd):
        if len(passwd) != 6:
            self.case_actual = "密码长度不等于6"
            return
        if user != "py37":
            self.case_actual = "用户名错误"
            return
        if passwd != "666666":
            self.case_actual = "密码错误"
            return
        if user == "py37" and passwd == "666666":
            self.case_actual = "登录成功"

    def case_res(self):
        if self.case_actual != self.case_expected:
            print("实际结果与预期结果不相符,用力不通过")
        else:
            print("恭喜,实际结果与预期结果相等,用例通过")
        print("实际结果为: {}".format(self.case_actual))
        print("预期结果为: {}".format(self.case_expected))


login_suc = LoginCase("登录成功", "登录成功")
login_suc.run_case("py37", "666666")
login_suc.case_res()


login_failed = LoginCase("登陆失败", "登陆失败")
login_failed.run_case("py37", "222233")
login_failed.case_res()

















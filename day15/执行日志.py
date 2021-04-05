
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


 在业务功能类当中,添加日志输出
 在使用这个类的时候,可以通过日志看到它的内部逻辑过程


"""

from day15.mylogger import logger


class LoginCase:

    def __init__(self, case_name, case_expected):
        logger.info("创建一条测试用例 用例名称为: {}".format(case_name))
        self.case_name = case_name
        self.case_expected = case_expected
        self.case_actual = None

    def run_case(self,user,passwd):
        logger.info("用例数据为: 用户名 {},密码 {}".format(user, passwd))
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
        logger.info("用力运行完成,运行结果为: {}".format(self.case_actual))

    def case_res(self):
        logger.info("开始结果比对")
        logger.info("实际结果为: {}".format(self.case_actual))
        logger.info("预期结果为: {}".format(self.case_expected))
        if self.case_actual != self.case_expected:
            logger.error("实际结果与预期结果不相符,用力不通过")
        else:
            logger.info("恭喜,实际结果与预期结果相等,用例通过")


login_suc = LoginCase("登录成功", "登录成功")
login_suc.run_case("py37", "666666")
login_suc.case_res()


login_failed = LoginCase("登陆失败", "登陆失败")
login_failed.run_case("py37", "222233")
login_failed.case_res()


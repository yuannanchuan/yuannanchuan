

from configparser import ConfigParser

conf =ConfigParser()

# 读取配置文件
conf.read("conf.ini", encoding="utf-8")

#读取log的name
value = conf.get("log", "name")
print(value)

# 读取mysql的port - 要是整数
value = conf.getint("mysql", "port")
print(type(value))
print(value)

class MyConf(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename,encoding="utf-8")


conf = Myconf("")






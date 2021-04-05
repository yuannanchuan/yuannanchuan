"""
从上到下 -

标准库: import 库名

第三方库: 官网文档都有显示如何导入 - copy过来

文件自定义导入:
    既可以导入模块名,也可以导入模块里面的内容(函数\全局变量)

如果导入模块名:
    如果相对于project的路径当中,有包
    form 包名[,包名.包名] import 模块名

    如果相对于project的路径当中,没有包
    import 模块名 [as 别名]

    导入之后,要使用模块当中的内容,则语法为:模块名(有别名用别名).变量\模块名(有别名用别名).函数(参数)


 如果导入模块名当中的内容(函数\全局变量\类):
    如果相对于project的路径当中,有包
    form 包名[,包名.包名] .模块名 import 函数\全局变量\类  [as 别名]

    如果相对于project的路径当中,没有包
    import 模块名  import 函数\全局变量\类 [as 别名]

额外提醒:
    同级目录下的文件,可以直接导入
    import myfunc



python找导入的文件的顺序和地方(sys模块, sys.path):
1.执行文件当前所在的目录
2.当前工程目录(时pycharm添加进去的)
3.python根目录下的lib目录(python安装时自带的标准库)
4.python根目录下的lib\site-packages(要手动通过pip命令安装的)

注意:模块取名的时候不要 跟你要用的 和标准库/第三方库重名.

pep8规范 - 导包顺序

标准库
第三方库
自定义库

导包要放在文件顶部

导包注意:不能2个模块互相导入

"""
import sys
import os
import xml


from day9导包_import import myfunc
import kedaibiao as kdb

"""
myfunc.deal(1,2,3,4)
print(kdb.moeny)
kdb.work()

# 找包的路劲
for item in sys.path:
    print(item)
"""

"""
from day9导包_import.myfunc import deal, money

deal(1, 2, 3, 4)
work()
"""













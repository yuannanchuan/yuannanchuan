
"""
1.日志收集器
    定义日志收集器: 要从代码当中按照要求 收集对应的日志,并输出到渠道当中.
        1)要收集那个级别以上的日志?
        2)日志是要什么样的格式显示
        3)日志压迫输出到那些地方去


"""

import logging

# 第一步
#    创建一个日志收集器
logger = logging.getLogger("nmb_py37yqq")

# 第二步:
# 设定自定义要手机的日志级别,自定义日志格式,自定义输出渠道

# 设自定义要手机的日志级别
logger.setLevel(logging.INFO)

# 自定义日志格式(Formatter)
fmt_str = "%(asctime)s %(name)s %(levelname)s %(filename)s [%(lineno)d] %(message)s"

# 实例化一个日志格式类
formatter = logging.Formatter(fmt_str)

# 实例化渠道(Handle)
# 控制台(StreamHandle)
handle1 = logging.StreamHandler()

# 设置渠道当中的日志显示格式
handle1.setFormatter(formatter)

# 将渠道与日志收集器绑定起来
logger.addHandler(handle1)

# 文件渠道(FileHandle)
handle2 = logging.FileHandler("py37日志.log",encoding="utf-8")
# 设置渠道当中的日志显示格式
handle2.setFormatter(formatter)
# 将渠道与日志收集器绑定起来
logger.addHandler(handle2)

# 文件渠道(FileHandle)
handle3 = logging.FileHandler("py37ERROR级别.log",encoding="utf-8")
# 设置渠道当中的日志显示格式
handle3.setFormatter(formatter)
# 设置handle3的日志输出级别为ERROR
handle3.setLevel(logging.ERROR)
# 将渠道与日志收集器绑定起来
logger.addHandler(handle3)

logger.info("hello,logging")
logger.warning("hello,debug")
logger.error("你有问题哟")













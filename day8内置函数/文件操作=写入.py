"""
write写入:如果文件存在,就打开,会清除之前已写入的内容,从头开始写.
        如果文件不存在,重新创建一个
        如果文件完整路径当中的某个目录不存在,会报错


1.打开文件 - 以写入模式打开.   mode = w
2.write
3.关闭文件


"""

fs = open(r"D:\SoftWare\ProgramFiles\Python\Python38-32\PY37期袁南川\day8内置函数\py37-写入.txt", mode="w", encoding="utf-8")


fs.write("66666\n")
fs.write("hello world\n")
fs.write("我想回家吃饭\n")

datalist = ["喜喜\n", "哈哈\n", "哎呀\n"]
fs.writelines(datalist)


fs.close()
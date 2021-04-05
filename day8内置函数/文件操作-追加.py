"""
append写入:如果文件存在,就打开,直接在文件末尾,接着写入
          如果文件不存在,重新创建一个
          如果文件完整路径当中的某个目录不存在,会报错


1.打开文件 - 以写入模式打开.   mode = a
2.write
3.关闭文件

"""

fs = open(r"D:\SoftWare\ProgramFiles\Python\Python38-32\PY37期袁南川\day8内置函数\py37.txt", mode="a", encoding="utf-8")

datalist = ["喜喜\n", "哈哈\n", "哎呀\n"]
fs.writelines(datalist)

fs.close()




"""
读取和看

fs = open(r"D:\SoftWare\ProgramFiles\Python\Python38-32\PY37期袁南川\day8内置函数\py37.txt", mode="a", encoding="utf-8")

datalist = ["喜喜\n", "哈哈\n", "哎呀\n"]
fs.writelines(datalist)

fs.close()

fs = open(r"D:\SoftWare\ProgramFiles\Python\Python38-32\PY37期袁南川\day8内置函数\py37.txt",  encoding="utf-8")

data = fs.read()
print("读取的数据为: ", data)

"""


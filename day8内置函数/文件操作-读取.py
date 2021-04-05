
"""
os模块 -

读写文件 - 不管是从文件读取出来,还是写入到文件当中,都是以字符串的形式

open函数 - 打开文件,读写追加模式
    open(文件路径,mode=模式,encoding="utf-8")
读数据:
        fs.read()
        fs.readlines()



追加:在末尾追加
写入:覆盖之前的内容

同级目录:相对路径

"""
# 以只读模式,打开文件,读取数据,文件的完整路径必须存在,不然会报错

fs = open(r"D:\SoftWare\ProgramFiles\Python\Python38-32\PY37期袁南川\day8内置函数\py37.txt", encoding="utf-8")

# 读取数据 - fs.read() 全部读取
data = fs.read()
print(data)

'''

print(---------)
data = fs.read()
print(data)
'''

# 读取数据  - 按行读取 fs.readline() / fs.readlines()

data = fs.readlines()
print(data)
# s = "1234\n"
# new_s = s.strip("\n").strip("aaaa")
# print(new_s)




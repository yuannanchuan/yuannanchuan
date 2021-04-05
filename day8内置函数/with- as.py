"""
不需要手动调用fs.close()
可以自动帮你关闭文件


"""
with open(r"D:\SoftWare\ProgramFiles\Python\Python38-32\PY37期袁南川\day8内置函数\py37.txt", mode="a", encoding="utf-8") as fs:
    fs.write("娜娜\n")
    fs.write("饭饭\n雷神\n囡囡\nso")
    fs.write("丫丫\n陪陪\n哎呀\nmanfu")


with open(r"D:\SoftWare\ProgramFiles\Python\Python38-32\PY37期袁南川\day8内置函数\py37.txt",  encoding="utf-8") as fs:
    data = fs.read()
    print(data)






"""
局部变量:函数内部定义的变量
全局变量:全局可用

关键字 : global


"""
bb = "hello"


def hellpworld():
    global bb
    a = 100
    print(a)
    print(bb)
    bb = 2000 #定义了一个变量的bb,赋值2000


#print(a)
hellpworld()
print("打印bb", bb)



"""
if __name__ == '__main__':
   #测试代码
    #当我们运行当前文件的时候,是以当前作为主入口,就会进入这里
   # 好处: 当前文件被其它模块导入使用时,此处的代码不会执行
    deal(66, 66, 66, 66)

"""
money = 200

def deal(*args):
    sum = 1
    print(args)
    for item in args:
        sum *= item
    left = sum % 20
    print("对20取余结果为: {}".format(left))


print("文件当中直接调用")
deal(66, 66, 66, 66)



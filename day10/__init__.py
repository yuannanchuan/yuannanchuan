
num = input("请输入一个数字")

try:
    res = 100 / int(num)
except:
    # 你抓到了异常,你自己额外添加的处理
    print("输入内容有误,请输入非0的数字!不能输入0或者其他非数字")
    # 你处理完了后,把错误又抛出给python解释器
    raise
else: # tey里面的语句没报错
    print(res)

finally:
    # 不管try里面有没有报错,最后一定会执行的代码
    print("我是一定会执行的代码")



print("6886576576")


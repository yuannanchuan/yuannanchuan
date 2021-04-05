num = input("请输入一个数字")

try:
    res = 100 / int(num)
except: # tey里面的语句报错了
    # 你抓到了异常,你自己额外添加的处理
    print("输入内容有误,请输入非0的数字!不能输入0或者其他非数字")
    # 你处理完了后,把错误又抛出给python解释器
    raise
"""
except ValueError as e:
    print("输入有误,请输入数字类类型!")
    print(e)

except Exception as e:
    print("其它未知错误")
    print(e)
"""











"""
函数 : 输入 - 参数
      输出 - 返回值 - return


1.怎么表达返回值
2. 什么情况虚下我需要返回?


return的作用:
1.函数的输出, 返回的类型可以时任意的类型
2.一旦再执行函数的过程种,遇到了return的语句,直接退出函数.
3.如果函数当中没有return,那么函数的返回是null
4.在定义函数时,如果希望某些条件没有满足,戒指退出函数的话,就用return.

调用函数的时候拿返回值
变量(接收返回值) = 函数调用

"""

def get_money_form_ATM(cardNm, passwd, need_money):

    if need_money > 1000:
        print("您的余额不足1000")
        print("没有钱返回")
        has_money = False
    else:
        has_money = True
        return need_money #函数执行的过程中,返回的值
    print("我取到钱了码?{]".format(has_money))


money = get_money_form_ATM("123456"."123456",800)  #money接受返回值
print("我取到了 {] 块钱,准备去买买买买买买了".format(money))






"""
#没有return的时候返回的值是null
def get_money_form_ATM(cardNm, passwd, need_money):
    if need_money > 1000:
        print("您的余额不足1000")
        print("没有钱返回")
        has_money = False
    else:
        has_money = True

    print("我取到钱了码?{]".format(has_money))


money = get_money_form_ATM("123456"."123456",800)  # money接受返回值
print("我取到了 {] 块钱,准备去买买买买买买了".format(money))




def get_money_from_ATM(cardNo, passwd, need_money):
      if need_money > 1000:
         print("您的余额不足1000")
         print("没有钱返回")
         has_money = False
      else:
         has_money = True
         return need_money  # 函数执行的过程当中，返回的值

      print("我取到钱了吗？{}".format(has_money))


 money = get_money_from_ATM("123456","123456",800)  # money接收返回值
 print("我取到了 {} 块钱。准备去买买买了。".format(money))
"""
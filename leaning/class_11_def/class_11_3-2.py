#5.函数参数类型：位置参数、默认值参数、动态参数、关键字参数
# 默认值参数

# 1.默认值参数，必须放在位置参数（非默认值参数）之后
# 2.默认值参数可以有多个，在遵守第1条的前提下
# 3.默认值参数调用时可以不传值。（不传：使用默认值；传值，使用传入的值）
# 4.按照顺序赋值，也可以通过关键字指定来赋值。

# 实例1：
# def greet(name,content):
#     print(name+content)
#
# greet("华华","你好")
#改造1：给参数添加默认值
# def greet(name,content='你好'):
#     print(name+content)
#
# greet("华华") #带默认值的参数可以不传
# greet("华华","你好呀，啦啦啦")
#改造2：默认值参数，放到位置参数前
# def greet(content='你好',name):
#     print(name+content)
#
# greet("华华")
# greet("吃了吗","华华")  #给默认值参数传了值也不行
# 会报错 SyntaxError: non-default argument follows default argument
# 改造3：多个默认值参数
def greet(name="华华",content='你好'):
    print(name+content)

greet()
greet(content="吃了吗？",name="小简老师") #如果不按照顺序赋值，需要关键字指定。



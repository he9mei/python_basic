#5.函数参数类型：位置参数、默认值参数、动态参数、关键字参数
# 动态参数

# 动态参数，又叫做不定长参数，即参数的个数是不确定的
# 动态参数格式：*变量名 如*args 即arguments参数
# *代表是动态参数，args是自己定义的，也可以是别的，但是通用是args
# 什么时候使用动态参数？不确定参数个数的时候

# 实例1：
def print_msg(*args):
    # print(*args)  # 使用动态参数时，不需要再带*
    print(args)
    print("args的类型是：",type(args))

print_msg(1,2,3,4,5)
# 结果是：动态参数生成元组形式
# (1, 2, 3, 4, 5)
# args的类型是： <class 'tuple'>

# 实例2：对动态参数进行求和
def add(*args):
    sum = 0
    for item in args:
        sum+=item
    return sum

result=add(1,2,3,4,5)
print("求和结果是：",result)

# 不同类型参数结合使用
# 1.位置参数和动态参数结合使用---动态参数，需要放在位置参数之后
def greet(content,*args):
    # print(args,content)  #('华华', '小简', '多多') 早上好
    name = ""
    for item in args:
        # print(item,content)  #分条打印
        name+=item
        name+="、"
    print(name,content)   #拼接动态参数后，再打印

greet("早上好","华华","小简","多多")
# 改造：把动态参数放在位置参数前
# def greet(*args,content):
#     print(args,content)
# greet("华华","多多","早上好")
# 会报错 TypeError: greet() missing 1 required keyword-only argument: 'content'

# 2.默认值参数和动态参数结合使用
# ---默认值参数，如果放在动态参数之前，需要重新传值（否则会把动态参数的值传给它）。无法取到默认值。
# ---默认值参数，如果放在动态参数之后，能取到默认值。但是无法重新传值（重新传值会传给动态参数）。
def greet(content="早上好",*args):
    print(args,content)
greet("华华","多多","小简")  # 结果：('多多', '小简') 华华
greet("晚上好","华华","多多","小简")  #结果：('华华', '多多', '小简') 晚上好

# 改造：把默认值参数放在动态参数之后
def greet(*args,content="早上好"):
    print(args,content)
greet("华华","多多","小简")  # 结果：('华华', '多多', '小简') 早上好
greet("华华","多多","小简","晚上好") #结果：('华华', '多多', '小简', '晚上好') 早上好





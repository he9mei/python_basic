#抛出异常
# python使用raise语句抛出一个指定的异常。我们可以使用类(Exception的子类)或实例参数调用raise语句引发异常。使用类时程序会自动创建实例。
# 使用raise可以输出更深层次的异常。在使用过程中，可以借助该方法得到更详细的异常信息。

# 实例：
# raise Exception  #抛出异常
# raise NameError  #抛出NameError异常
'''
try:
    raise NameError("this is NameError!")
except NameError:
    print("发生异常")  #不再抛出，结果：发生异常
    raise  #再次抛出，结果：NameError: this is NameError!
'''
# 我们前面碰到的NameError、SyntaxError等异常类称为内建异常类。python中，内建异常内很多。可以使用dir函数列出异常类的内容，
# 用在raise语句中，用法如raise NameError这般。
# print(dir(NameError))  #看不太懂

# python中常见的内建异常类
# Exception 常见错误的基类
# AtrributeError    对象没有这个属性
# IOError   输入/输出操作失败
# IndexError    序列中没有此索引(index)
# KeyError  映射中没有这个键
# NameError 未申明/初始化对象（没有属性）
# SyntaxError   python语法错误
# SystemError   一般解释器系统错误
# ValueError    传入无效参数
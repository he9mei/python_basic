#异常
# 捕捉异常
# 每一个异常都是一些类的实例，这些实例可以被引用，并且可以用很多方法进行捕捉，使得错误可以被处理，而不是整个程序失败。
# 处理程序中的异常，最简单的是使用try/except语句。
# try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。如果不想在发生异常时结束程序，只需在try语句捕获异常即可。
# 如果没有处理异常，异常就会被传播到调用的函数中。如果调用的函数中依然没有处理，异常就会继续传播，直到程序的最顶层。

# 语句格式：
# try:
#   语句块
# except 异常名字1：  #except 异常名字1 as e1： 也可以用as给异常名字1改名字
#   异常1处理语句块
# except 异常名字2：
#   异常2处理语句块
# else:
#   没有发生异常语句块
# finally:
#   不管是否发生异常都会执行的语句块

# 实例1：NameError
# print(a)  #NameError: name 'a' is not defined
'''
try:
    print(a)
except Exception as e:
    print("异常信息是：",e)  #异常信息是： name 'a' is not defined
'''
# 实例2：ZeroDivisionError
# print(2/0)  #ZeroDivisionError: division by zero

def exp(x,y):
    try:
        a=x/y
        print(a)
    except Exception as e:
        print(e)
# exp(2,1)
exp(2,0) #division by zero





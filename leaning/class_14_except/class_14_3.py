#捕捉多个异常
#1.一个try语句对应多个except子句
# python支持在一个try/except语句中处理多个异常。
# 一个try语句可能包含多个except子句，分别处理不同的异常，但是最多只有一个分支会被执行。
# 处理程序只针对对应try子句中的异常进行处理，而不会处理其他异常语句中的异常。
# 为什么不用if语句，如用if判断被除数不能为0？
# 需要考虑很多情况，也需要写很多if语句，若不经过严密思考和大量测试，很难把所有情况考虑到。此外if语句会使程序阅读困难。
# 抛出异常的方式更简单、直观，可以清晰帮助用户定位问题，并且可以自定义异常信息，进一步定位问题所在。

# 实例：
def exp(x,y):
    try:
        a=x/y
        b=name
        return a,b
    except NameError:
        print("this is NameError!")
    except ZeroDivisionError:
        print("this is ZeroDivisionError!")
# print(exp(2,1)) #this is NameError!
print(exp(2,0))  #this is ZeroDivisionError!


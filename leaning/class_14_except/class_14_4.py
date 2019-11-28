#捕捉多个异常
#2.使用一个块捕捉多个异常
# 如果需要使用一个块捕捉多个类型的异常，可以将它们作为元组列出。使用该方式时，遇到的异常类型是元组中的任意一个，都会走异常流程。
# 好处：如果希望多个except子句输出同样的信息，就没有必要在多个except子句中重复输入语句，写在一个块即可。

# 实例：
def exp(x,y):
    try:
        a=x/y
        b=name
        return a,b
    except (NameError,ZeroDivisionError,TypeError):  #异常名字作为元组列出
        print("one of NameError,ZeroDivisionError")
exp(2,1)  #one of NameError,ZeroDivisionError
exp(2,0)  #one of NameError,ZeroDivisionError



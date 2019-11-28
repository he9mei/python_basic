#全捕捉

# 实例：调用函数时有一个实参传入的是空值。
def exp(x,y):
    try:
        a=x/y
        b=name
        return a,b
    except (NameError,ZeroDivisionError,TypeError) as e:
        print(e)
exp(2,"")  #unsupported operand type(s) for /: 'int' and 'str'
#在编码过程中，即使程序能处理好几种类型的异常，但有一些异常还是会从我们手中溜走。上面实例的异常就逃过了try/except语句的检查，
# 这种情况下，与其使用不是捕捉异常的try/except语句隐藏异常，不如让程序立即崩溃。
# 实例2：全捕捉
# 可以在except子句中忽略所有异常类，从而让程序输出自己定义的异常信息。
# 但是这只是一种可参考的解决方式，实用性来讲，不建议这么做，因为这样捕捉异常非常危险，会隐藏所有没有预先想到的错误。
# 建议使用抛出异常的方式处理，或者对异常对象e进行一些检查。
def exp(x,y):
    try:
        a=x/y
        b=name
        return a,b
    except:
        print("发生异常！")
exp(2,"")



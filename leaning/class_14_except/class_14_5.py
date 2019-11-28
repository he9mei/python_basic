#捕捉对象
# 如果希望在except子句中访问异常对象本身，也就是看到一个异常对象真正的异常信息，而不是输出自定义的异常信息，可以使用as e的形式，
# 我们称之为捕捉对象。

# 实例：
def exp(x,y):
    try:
        a=x/y
        b=name
        return a,b
    except (NameError,ZeroDivisionError,TypeError) as e:
        print(e)
# exp(2,1)  #name 'name' is not defined
exp(2,0)  #division by zero

# 结果可知，执行过程中抛出的异常被截获并正常输出了相关信息，并且使用这种方式可以捕捉多个异常。

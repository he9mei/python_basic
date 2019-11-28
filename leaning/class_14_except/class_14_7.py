#异常中的else
# try...except...else
# 如果在try子句执行时没有发生异常，就会执行else语句后的语句(如果有else)。
# 使用else语句比把所有语句放在try字句里面更好，这样可以避免一些意想不到而except又没有捕获到的异常。

# 实例：
def exp(x,y):
    try:
        a=x/y
        print(a)
        # return a  #注意：如果用了return语句，else就不会再执行了。
    except Exception as e:
        print(e)
    else:
        print("try语句没有异常。")
exp(2,1)  #try语句没有异常。

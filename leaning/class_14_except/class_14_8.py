#异常中的finally子句
# python中的finally字句需要和try子句一起使用。try/finally语句无论是否发生异常都将执行最后的代码。
# 在finally的异常处理程序中，finally中的子句一定是最后执行的。finally字句在关闭文件和数据库连接时非常有用。
# try...finally...
# try...except...finally...
# try...except...else...finally...

# 实例1：
'''
def exp(x,y):
    try:
        a=x/y
    finally:
        print("无论是否报错，都会执行！")
exp(2,0)
'''
# 实例2：
def exp(x,y):
    try:
        a=x/y
    except Exception as e:
        print(e)
    finally:
        print("无论是否报错，都会执行！")
exp(2,0)

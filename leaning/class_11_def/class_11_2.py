#4.return关键字

#return的作用：当你调用这个函数的时候，会返回一个结果。
#这个结果你拿到之后，可以做进一步的处理。
#return后面0个参数，返回的就是None
#return后面1个参数，返回的就是你指定的参数，参数什么类型，返回的就是什么类型
#retuen后面多个参数>1，返回的参数会放在一个元组里面
#什么时候用return：如果想拿到某个函数的运行结果，就用return。
#注意：return相当于一个结束信号，当函数遇到return，后面的代码将不在执行。

# 实例1
def add1():
    print(1+2)
    return #隐式的添加一个return，但是return后面没有任何表达式，返回None

def add2():
    return 1+2

# 调用函数
print("***第1个函数***")
# add1()
print("第1个函数的结果：",add1())
print("***第2个函数***")
# result=add2()+20
# print(result)
print("第2个函数的结果：",add2())

# 实例2：
# 利用for循环、range函数，编写任意整数序列的求和函数
#求和1-10
def add():
    sum = 0
    for item in range(1, 11, 1):
        sum += item
    # print("求和结果是：{}".format(sum))
    # return sum
    return sum,666  #多加了一个参数

result=add()
print("求和结果是：",result)



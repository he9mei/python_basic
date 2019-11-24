#5.函数参数类型：位置参数、默认值参数、动态参数、关键字参数
# 位置参数

# 实例1：
def print_msg(a,b):  #形参
    print(a)
    print(b)

print_msg("hello","python")  #实参

# 位置参数总结：
# 1.有个位置参数就传递几个，不能多不能少
# print_msg(1,2,3)
# 参数多了，会报错
# TypeError: print_msg() takes 2 positional arguments but 3 were given
# print_msg(1)
#参数少了，也会报错
# TypeError: print_msg() missing 1 required positional argument: 'b'
# 2.按顺序赋值
# 3.传递参数的使用顺序不一定按照传递顺序
# 4.参数不一定都会使用
# 5.可以不按照顺序赋值，通过关键字指明，通过形参的指定取赋值。
# 实例2：
def print_msg(a,b):  #形参
    print("a参数的值是：",a)
    print("b参数的值是：",b)

print_msg(b="hello",a="python")  #实参

# 练习：通过for循环和range函数，写出任意连续整数序列求和的函数
#实例3：
def add(m,n,k):
    sum=0
    for item in range(m,n,k):
        sum+=item
    # print("求和结果是：",sum)
    return sum

# add(1,101,1)  #1-100求和
# add(0,101,2)  #1-100偶数求和
# add(1,101,2)  #1-100奇数求和
result=add(1,101,1)
print("求和结果是：",result)

#总结：三步函数法
#1.先用零散的代码写出功能要求
#2.编程函数 def 函数名()
#3.提高复用性，参数化
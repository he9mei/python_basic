#python之for循环-2

#range()函数与for循环结合使用

#先复习下字符串的切片
# s="lemon"
# print(s[1:3:1])  #切片

#rang[m,n,k]    m开头，n结尾，k步长，取头不取尾
#作用：生成一个整数序列

# print(list(range(0,11,2)))  #0-10的偶数，结果：[0, 2, 4, 6, 8, 10]
#默认k=1
# print(list(range(1,6)))  #1-5的整数，结果：[1, 2, 3, 4, 5]
#默认m=0,k=1,只传一个n
# print(list(range(6))) #0-5的整数，结果：[0, 1, 2, 3, 4, 5]

#练习题1：利用range函数和for循环，完成1-100的和
sum=0
for item in range(1,101):
    sum+=item
# print("1-100的和是：",sum) //字符串与数字拼接不能用+，可以用，
print("1-100的和是：{}".format(sum))

#练习题2：利用range函数和for循环，完成某个数组的倒序输出
s=[1,2,3,4,5,6,7]  #index: 0-6
for item in range(6,-1,-1):
    print("输出结果是：{}".format(s[item]))

#正序
# for item in range(0,7,1):
#     print("输出结果是：{}".format(s[item]))





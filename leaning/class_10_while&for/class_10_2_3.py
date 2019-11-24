#python之for循环-3

# 嵌套for循环

# 练习题1：输入二维数组列表里的每一个元素
# list=[[1,2,3],["lemon","python","华华"]]
# for item in list:
#     print("外层循环结果：{}".format(item))
#     for i in item:
#         print("内层循环结果：{}".format(i))

#练习题2：打印边长为5的直角等腰三角形
#*
#**
#***
#****
#*****
#
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")  #控制不换行输出
#     # print("这是第{}行".format(i))
#     print("")  #内循环结束后，换行

#练习题3：输出九九乘法表
#1*1=1
#2*1=2 2*2=4
#3*1=3 3*2=6 3*3=9
#...
#9*1=9 9*2=18 9*3=27 9*4=36 ... 9*9=81

for i in range(1,10):
    for j in range(1,i+1):
        # print(i,"*",j,"=",i*j," ",end="")  //或者使用格式化输出也可以
        print("{0}*{1}={2} ".format(i,j,i*j),end="")
    print("")

#i 和 j不仅控制着外循环和内循环的循环次数，也要考虑数据存在的关联
#练习2也可以改成
# for i in range(1,6):
#     for j in range(1,i+1):  #此处i和j只用来控制循环次数，没有数据关联，range中m=0开始也行。
#         print("*",end="")
#     print("")


#课后题：利用嵌套for循环，完成冒泡排序
# l=[1,12,5,28,3,105,99,88]



#课后题：利用嵌套for循环，完成冒泡排序
l=[1,12,5,28,3,105,99,88] #index: 0-7 8个数字
# print("原来数组是：{}".format(l))
# print("数组长度是：{}".format(len(l)))  #结果：8

for i in range(len(l)-1):  #0，7，1  取值0-6 执行7次，最后1个数不用再执行
    for j in range(len(l)-1-i):  #第1个数比较7次，第2个数比较6次，第3个数比较5次。。。
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    # print("第{0}次比较结果是:{1}".format(i+1,l))
print("升序排序后数组是：{}".format(l))

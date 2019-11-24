#python之while循环-2

#结合break以及continue防止while循环进入死循环
#while：break...continue...
#break 结束循环
#continue 结束本次循环，继续下一次循环

#while跟if结合使用，利用continue和break
a=10
while True:  #死循环必要条件
    if a>0:
        print("a的值是：{}".format(a))
        a-=1
        continue
    else:
        break




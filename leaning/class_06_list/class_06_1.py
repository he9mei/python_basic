#数据类型4-列表
#在python中是属于使用率最高的数据类型

#1.标志[] 关键字list
#2.a=[]空列表
#3.列表中的数据可以是任何类型:数字、字符串、元组、列表、字典
#4.列表的取值也是根据索引（操作同字符串）列表名[索引值]  正序/反序
#5.列表的切片（操作同字符串）列表名[m:n:k]
#6.判断元素in /not in（操作同字符串） 成员运算符

#a=[]  #类型返回list
#print(type(a))
a=[1,0.01,"lemon",(1,2,3),[4,5,6]]
print(a)
print(a[2])
print(a[-1])
print(a[1:4:2])
print([4,5,6] in a)
print(0.01 not in a)
print("lemon" in a)
#怎么取到1？
print(a[-2][0])  


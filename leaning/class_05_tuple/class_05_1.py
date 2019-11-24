#数据类型3-元组

#1.元组的标志 tuple
#2.元组只有一个数据时，需要在后面加逗号，否则就不是元组类型
#3.元组里面的数据可以是任意类型：数字、字符串、元组、列表、字典
#4.元组取值是根据索引取值，也分正序和反序（操作同字符串）元组名[索引值]
#5.元组切片（操作同字符串）tuple_1[1::2]
#6.元组的值一旦确定，就无法更改！增删改都不允许！
#7.判断元素in /not in （操作同字符串）

#tuple_1=()  #空元组，类型返回tuple
#tuple_1=(1)  #类型返回int
#tuple_1=(1,)  #类型返回tuple
#print(type(tuple_1))
tuple_1 = (1,0.99,"lemon",(1,2,3))
print(tuple_1[2])
print(tuple_1[-1])
print(tuple_1[-1][-1])  #根据索引多层取值
print(tuple_1[1::2])
#tuple_1[0]=2  #会报错
print(0.99 in tuple_1)
print("lemon" not in tuple_1)
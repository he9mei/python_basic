#数据类型2-字符串

#1.字符串取值方式 str[索引值]
a = "lemon"
print(a[2])
print(a[-1])

#2.怎么处理字符串里面的特殊字符 转义 加\或者r R
a = "hello\nlemon"
a = "hello\\nlemon"
a = r"hello\nlemon"
a = R"hello\nlemon"
print(a)

#3.字符串的运算
# +：字符串拼接
# *：字符串重复输出
a = "hello"
b = "lemon"
c = a+"  "+b #字符串拼接
print(c)
print(type(c))
print(a*3)  #字符串重复输出
#不同类型怎么拼接？
d = 123
#print(a+d) 会报错,需要把int类型转成str类型
print(a+str(d))

#4.in/not in：成员运算符，判断是否存在，返回布尔值 ture/false
a = "lemon"
print("l" in a)
print("t" in a)
print(type("t" in a))


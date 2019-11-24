#python运算符

#5.成员运算符 in  not in
#返回值是：布尔值 true false
#判断某个字符或元素是否存在与我们的字符串、元组、列表、字典
s="lemon"
l=[1,0.99,"lemon",[1,2,3]]
d={'name':'华华','age':18,'score':99.99}
print("n" in s)
print(0.99 not in l)
print(3 in l[-1])
print("n" not in l[2])
print("age" in d)  #字典是用key来定位元素
print(18 in d)  #返回false,直接找value定位不到
print(18 in d.values())  #判断value是否在字典中，可以这样写


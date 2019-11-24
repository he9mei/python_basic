#数据类型5-字典

#1.标志{} 关键字dict
#2.a={} 空字典
#3.字典的存储格式是 key:value 键值对
#4.字典里面value可以是任何类型的取值
#5.取值方式：根据key取值 字典名[key] （不能通过索引，因为字典是无序的）

# a={}
# print(type(a))  #返回类型 dict
a={"name":"华华","age":18,"money":99.99,"score":[99,100,88]}
print(a)
print(a["name"])

#问题：
#in/not in不确定是否适用于字典，返回都是false?还是用法不对？
# print('"name":"华华"' in a)  #报错
#解决：
print("name" in a)  #只能判断key是否包含在字典中
print("华华" in a.values())   #判断value是否包含在a中的话，可以这样写





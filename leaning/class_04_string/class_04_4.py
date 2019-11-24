#python字符串内建函数

#1.字符串的大小写切换upper(),lower()
str_1 = "lemon"
#str_1 = "leMOn"
str_2 = "LEMON"
#str_2 = "leMOn"
#res = str_1.upper()
res = str_2.lower()
print("转换后的结果:{}".format(res))

#2.字符串的查找 find()函数
#res = str_1.find("o")
#res = str_1.find("em")
res = str_1.find("py")
print("查找的结果:{}".format(res))
#单个字符，如果能找到，返回字符在字符串的索引值
#子字符串，如果能找到，返回子字符串第一个元素在原来字符串的索引值
#找不到，返回-1

#3.字符串的替换 replace()函数
str_3 = "happy"
#res = str_1.replace("o","@") #替换目标字符 新值
res = str_3.replace("p","开心") #所有目标字符都会替换
print("替换的结果:{}".format(res))

#4.字符串的切割 split()
str_4 = "lemono"
res = str_4.split("o") #返回列表类型数据，但是元素类型还是字符串
print("切割的结果:{}".format(res))

#5.字符串头尾处理 strip()函数
str_5 = "@@lem@on@@"
res = str_5.strip("@") #只处理头尾，中间的该字符是不处理的
print("处理后的结果是:{}".format(res))
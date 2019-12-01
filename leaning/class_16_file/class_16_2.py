# 文件操作

# 2.文件读和写
# open函数返回的是一个file对象，有了file对象，就可以开始读取内容。
# （1）读取read()
# 如果希望整个文件的内容读取为一个字符串值，可以使用File对象的read()方法。
# read()方法是从一个打开的文件中读取字符串，可以是二进制数据，而不仅仅是文字。从文件开头开始读入。
# fieObject.read([count])    count参数是从已打开的文件中读取的字节计数，不传即会尽可能多的读取。
path = "D:\\hehuaimei\\python_file_test.txt"
'''
file_test = open(path, "r")
print("读取到的内容是：", file_test.read(5))     # 读取到的内容是： hello
print("读取到的内容是：", file_test.read())  # 读取到的内容是：  python!welcom!
'''
# 备注：多次连续调用read()是接着读取的。

# (2)写入write()
# 在Python中用write()方法向一个文件写入数据。可以将任何字符串写入一个打开的文件。
# write()方法不会在字符串结尾添加换行符("\n")
# fileObject.write(string)  string参数是需要写入的内容
# write()函数返回的是写入文件的字符串的长度
'''
file_test = open(path, 'w')
print("写入的长度是：", file_test.write("what are you doing?"))  # 写入的长度是： 19
file_test = open(path, "r")
print("写入的结果是：", file_test.read())  # 写入的结果是： what are you doing?
'''
# 备注：写完之后再读取，需要重新打开。
# write()的处理方式是覆盖原有文件，如果要追加用什么呢?打开文件模式用"a"
'''
file_test = open(path, 'a')
print("追加的长度是：", file_test.write("\nwhat are you doing?"))  # 写入的长度是： 19
file_test = open(path, "r")
print("追加的结果是：", file_test.read())
# 写入的结果是： what are you doing?what are you doing?
'''
# 备注：如果传递给open函数的文件不存在，写入和追加模式就会创建一个新的空文件。
# 在python中，用\n表示换行。可以在以上追加文字前加上\n换行。
# 如果需要读写特定编码的文本，需要给open传入encoding参数。如file_test=open(path,'r',encoding="gbk")

# (3)读写行readline()\readines()\wrtelines()
# readline()方法会读取单独一行，换行符为\n。如果返回空字符串，说明已经读到最后一行了。
# readlnes()输出结果为一个字符串的列表，并且换行符也会被输出。
'''
file_test=open(path, 'w')
file_test.write("hello\n")
file_test=open(path, 'a')
file_test.write("python")
file_test=open(path, 'r')
# print("读取一行:", file_test.readline())  # 读取一行: hello
print("读取多行:", file_test.readlines())  # 读取多行: ['hello\n', 'python']
'''
# writelines()
file_test=open(path, 'w')
str_lines=["hello\n", "python\n ", "welcom!"]
file_test.writelines(str_lines)
file_test=open(path,'r')
print("多行写入结果是：\n", file_test.read())

# (4)关闭文件

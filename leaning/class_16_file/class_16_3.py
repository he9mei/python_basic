# 3.对文件内容进行迭代
# 在实际应用中，对文件内容进行迭代和重复操作是比较常见的。所谓迭代就是不断重复某一动作，直到这些动作都完成。

# （1）按字节处理
# 在while循环中，read()方法是最常见的对文件内容进行迭代的方法。
'''
path = "D:\\hehuaimei\\python_file_test.txt"
file_test = open(path, 'w')
file_test.write("hello")
file_test = open(path, 'r')
# c=file_test.read(1)
# while c:
#     print(c)
#     c=file_test.read(1)
# file_test.close()
# 备注：运行大文件末尾会返回空字符串，为false；在这之前都返回非空字符串，为true。
# while true/break 改写
while True:  # True要首字母大写
    c=file_test.read(1)
    if not c:
        break
    print(c)
file_test.close()
'''

# （2）按行操作
# 实际操作中可能需要对文件的行进行迭代，而不是单个字符。需要使用readline方法。
'''
path = "D:\\hehuaimei\\python_file_test.txt"
file_test=open(path, 'w')
file_test.writelines(["hello\n", "python\n", "welcom!"])
file_test=open(path, 'r')
while True:
    line=file_test.readline()
    if not line:
        break
    print(line)
'''
# (3)fileinput实现懒加载迭代
# read方法和readlines方法，不带参数时将读取文件所有内容，然后加载到内存中。文件很大时，可能造成内存溢出。
# 这种情况下可以考虑使用while循环和readline方法代替。
# 在Python中for循环是优先考虑的选择，意味着对任务进行分隔操作，而不是一步到位。
# 按行读取文件时，若能使用for循环，则称之为懒加载迭代，因为在操作过程中只读实际需要的文件部分。
'''
path = "D:\\hehuaimei\\python_file_test.txt"
import fileinput
for line in fileinput.input(path):
    print(line)
'''

# (4)文件迭代器
# 文件对象是可迭代的，意味着可以直接在for循环中使用文件对象。
# 使用for循环对文件对象进行迭代，结束后要显示关闭文件对象。
path = "D:\\hehuaimei\\python_file_test.txt"
file_test=open(path, 'r')
for line in file_test:
    print(line)
file_test.close()

# 4.StringIO函数---未详细练习
# 数据的读取除了通过文件，还可以在内存中进行。python中iO模块提供了str操作的StringIO函数。
# 5.序列化和反序列化---未详细练习
# 在运行程序过程中，所有变量都在内存中，我们把变量从内存中变成可存储或传输的过程称之为序列化。
# 反过来，把变量内容从序列化对象重新读到内存中称为反序列化。



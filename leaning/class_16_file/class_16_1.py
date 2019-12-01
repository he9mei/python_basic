# 文件操作

# 1.打开文件
# open(file_name[,access_mode][,buffering])   返回一个文件对象
# file_name变量：带路径的文件名
# access_mode变量：指打开文件的模式，有只读、写入、追加等。默认模式是r只读模式。
# buffering变量：如果buffering的值为0就不会寄存；值为1就会寄存；大于1的整数表示寄存区缓冲大小；负值表示缓冲大小就是系统默认值。
path = "D:\\hehuaimei\\python_file_test.txt"  # \进行转义
file_test = open(path)
print(file_test.name)  # D:\hehuaimei\python_file_test.txt
# 路径补充：绝对路径是从根文件夹开始；相对路径是相对于当前工作目录的路径，用"."号代替这个路径值。

# 附加打开文件模式：
# r只读 rb二进制打开，只读 r+读写 rb+
# w只写 wb二进制打开，只写 w+读写，已存在覆盖，不存在创建 wb+
# a追加 ab二进制打开，追加 a+读写，已存在追加，不存在创建 ab+




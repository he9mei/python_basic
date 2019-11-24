#python格式化输出

name = "lemon"
age = 18
#print(name+"今年"+age+"岁") 会报错
print(name+"今年"+str(age)+"岁") #int转str

#以下使用格式化输出
# 第一种格式化输出 %d %f %s
print("%s今年%d岁"%(name,age))
score = 99.99
print("%s今年%d岁，数学考了%f分！"%(name,age,score)) # %f 默认保留6位小数
print("%s今年%d岁，数学考了%.2f分！"%(name,age,score)) # %.2f 保留2位小数
print("%s今年%d岁，数学考了%s分！"%(name,age,score))
#%d只能放整数，%f可以放整数、浮点数，%s可以放任何值

#第2中格式化输出 {} format
#{}里面可以指定取值索引，如果不指定则默认按照顺序取值；
# format内数据-索引从0开始
print("{}今年{}岁，数学考了{}分！".format(name,age,score))
print("{1}今年{2}岁，数学考了{0}分！".format(name,age,score)) #指定取值顺序


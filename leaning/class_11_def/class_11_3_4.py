#5.函数参数类型：位置参数、默认值参数、动态参数、关键字参数
# 关键字参数

# 关键字参数-格式：**kwargs  -->key words arguments
# 关键字参数-类型：key-value

# 实例1：
def info(**kwargs):
    print("info信息是：",kwargs)
    print("kwargs类型是：",type(kwargs))  #kwargs类型是： <class 'dict'>
    for item in kwargs.values():  #打印关键字参数生成的字典的所有value
        print(item)

info(name="华华",age=18,sex="female") #info信息是： {'name': '华华', 'age': 18, 'sex': 'female'}

# 实例2：结合位置参数---关键字参数，必须放在位置参数之后
def info(cource,**kwargs):
    print("课程是：",cource)
    print("kwargs信息是：",kwargs)
info("python",name="huahua",age=18,sex="female")

# def info(**kwargs,cource):  位置参数放在关键字参数后，会报错 SyntaxError: invalid syntax

# 实例3：结合默认值参数---关键字参数，必须放在默认值参数之后
def info(cource="java",**kwargs):
    print("课程是：",cource)
    print("kwargs信息是：",kwargs)
info(name="huahua",age=18,sex="female")
info("python",name="huahua",age=18,sex="female")

# def info(**kwargs,cource="java"): #默认值参数放在关键字参数之后，会报错 SyntaxError: invalid syntax

# 补充：from书籍
# 实例4：动态参数直接传入元组，关键字参数直接传入字典
t=(1,2,3,4)
d={"name":"huahua","age":18,"sex":"female"}
def personal_info(*args,**kwargs):
    print("动态参数是：{}".format(args))
    print("关键字参数是：{}".format(kwargs))
personal_info(*t,**d)

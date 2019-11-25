#python类与对象

# 类里面的方法
# 构造方法/初始化方法-1
# 1.__init__（）是initialization的简写，是初始化的意思，又叫做构造方法。
# 2.在python中__init__（）方法是一个特殊的方法，在对象实例化时被调用。
# 3.在定义类时，如果不显示定义一个__init__()方法，则程序默认调用一个无参的__init__()方法。
# 4.一个类中可以定义多个构造方法，但是实例化时只实例化最后一个构造方法，即后面的构造方法会覆盖前面的构造方法，
# 并且需要根据最后一个构造方法的形式进行实例化。建议一个类中只定义一个构造方法。

# 实例1：显示定义一个，传参构造方法
# class BoyFriend:  #类名后面，如果没有明确的继承类，可以不写，也可以写(object)，所有类都继承object。
class BoyFriend(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def code(self):
        print("{},{},会写代码！".format(self.name,self.age))
bf=BoyFriend("jackson",18)  #构造方法有参数，创建实例时需要传相应的参数
# bf=BoyFriend() #如果创建实例不传参数会报错
print(bf.name)
bf.code()

# 实例2：显示定义一个，无参数构造方法
class BoyFriend:
    def __init__(self):
        print("这是一个无参的构造方法。")
    def code(self):
        print("男朋友会写代码。")
bf=BoyFriend()
print("实例化结束。")
bf.code()

# 实例3：不显示定义构造方法
class BoyFriend:
    def code(self):
        print("男朋友会写代码。")
bf=BoyFriend()  #没有显示定义构造方法，实例化过程中会调用默认的构造方法，不会输出任何内容。
print("实例化结束。")
bf.code()

# 实例4：显示定义多个构造方法
class BoyFriend:
    def __init__(self):
        print("这是一个无参的构造方法。")
    def __init__(self,name,age):
        print("这是一个有参的构造方法。")
        self.name=name
        self.age=age
    def code(self):
        print("男朋友会写代码。")
# bf=BoyFriend()  #会报错，因为最后一个构造方法是有参数的
bf=BoyFriend("jackson",18)
print("实例化结束。")
bf.code()


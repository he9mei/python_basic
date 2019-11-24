#python类与对象

#类里面的函数/方法

# 1.类函数/类方法 @classmethod 可以通过类名直接调用
# 什么时候取定义为类方法呢？
# （1）如果想直接通过 类名.函数名() 调用
# （2）方法跟属性没有直接关联，不能直接调用属性
# （3）当我们有初始化函数时，可以直接定义为类方法
# 2.实例函数/实例方法
# 3.静态函数/静态方法 #staticmethod 可以通过类名直接调用 也适用于类方法的那3条

# 实例：
class BoyFriend:
    height=180
    age=28
    @classmethod  #类方法
    def swimming(cls):  #可以不用self实例参数（也可以用） #问题：不能没有任何参数？否则会报错。cls代表什么？
        print("会游泳")
        # print(self.age)  #类方法，如果不用self实例，无法调用属性
    def coking(self):  #实例方法
        print("会做饭")
        # print(self.age)  #方法内调用属性，需要self实例
    @staticmethod
    def hiking():  #静态方法，不要self参数，否则会报错；可以没有任何参数
        print("会爬山")

BoyFriend.swimming()  #类方法，可以直接通过类名调用
BoyFriend().swimming()
# BoyFriend.coking()  #会报错
BoyFriend().coking()  #实例方法，则必须通过实例调用，或者传入实例参数
# BoyFriend.coking(BoyFriend())
BoyFriend.hiking() #静态方法，可以直接通过类名调用
BoyFriend().hiking()

# 总结：类方法、实例方法、静态方法
# 1.都可以被谁调用
# 2.只有静态方法、类方法，可以直接通过 类名.函数名() 调用
# 3.静态方法、类方法，不能调用类属性

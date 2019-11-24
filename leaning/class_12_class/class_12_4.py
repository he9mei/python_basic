#python类与对象

# 类里面方法

# 调用属性、参数化
# 调用属性(只有实例方法可以；静态方法和类方法，不可以调用属性)
# 参数化(不管什么方法，都可以参数化)

class BoyFriend:
    name="jackson"
    height=180
    age=28
    @classmethod
    def swimming(cls):
        print("会游泳")
    @staticmethod
    def hiking():
        print("会爬山")
    def coking(self):
        print(self.name,"会做饭")  #实例方法，调用属性
    # def coding(self,sex,language="java"):  #参数化-位置参数、默认值参数
    #     print(self.name+",{0},会写{1}代码".format(sex,language))
    def coding(self,*args):  #参数化-动态参数
        print(self.name+"会写{}代码".format(args))

bf=BoyFriend()
bf.coking()
# bf.coding("male")
# bf.coding("male","python")
bf.coding("java","python")

# 总结：
# 实例方法：
# 如果调用类里面的属性 self.属性名
# 如果实例方法带参数，参数的传递，同普通的函数。

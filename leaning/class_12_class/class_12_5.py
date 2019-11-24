# python类与对象

# 类里面方法

# 方法之间的调用
# return返回值

class BoyFriend:
    name = "jackson"
    height = 180
    age = 28

    def swimming(self, long):
        print(self.name + "能连续游泳{}米".format(long))

    def coding(self, long, *args):
        # print("会代码")
        self.swimming(long)  # 实例方法内，调用类里面的其他方法
        # return (self.name+"会写代码")
        # return (self.name+"会写{}代码".format(language))
        return (self.name + "会写{}代码".format(args))


bf = BoyFriend()
# bf.coding()
result = bf.coding(1000, "python", "java")
print(result)

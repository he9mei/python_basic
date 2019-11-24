#python类与对象
#self关键字

#还是用上节课的实例
class BoyFriend:
    height=180
    age=28
    def swimming(self):  #类里面函数与普通函数的区别，就是self
        print("会游泳")
        print(self)  #self为何物？<__main__.BoyFriend object at 0x1020b8e50>
    def coking(self):
        print("会做饭")
    def hiking(self):
        print("会爬山")

BoyFriend().swimming()
print(BoyFriend())  #打印实例对象 <__main__.BoyFriend object at 0x101c8be50>  后面是内存地址
# 结论：打印实例对象和打印self结果相同，说明self实际上就是一个实例

# 直接以实例调用
bf=BoyFriend()
bf.coking()

#把实例作为参数传递
bf=BoyFriend  #没有创建实例
# bf.coking()  #报错 TypeError: coking() missing 1 required positional argument: 'self'
bf.coking(BoyFriend())


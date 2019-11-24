#python类与对象
# 关键字 class 类里面一般包含属性以及函数
# class 类名：
#   '''类的注释'''
#   属性
#   函数

# 实例1：
class BoyFriend:  #类名使用驼峰命名
    #属性（即变量）
    height=180
    age=28
    #函数---与普通函数80%相似,新增self概念
    def swimming(self):
        print("会游泳")
    def coking(self):
        print("会做饭")
    def hiking(self):
        print("会爬山")

# 怎么调用类里面的属性和函数呢？---通过实例/对象
# 怎么创建实例？---类名()
# 怎么调用方法？---实例.方法
# 怎么调用属性？---实例.属性

bf=BoyFriend()  #创建实例
bf.swimming()   #调用方法
print(bf.age)   #调用属性

bf_2=BoyFriend()  #创建第2个实例
bf_2.coking()



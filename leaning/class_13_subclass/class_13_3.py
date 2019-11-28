#封装
# 1.封装是全局作用域中其他区域隐藏多余信息的原则。听起来有些像多态，使用对象而不用知道其内部细节。
# 它们都是抽象原则，都会帮助处理组件而不用过多关心细节，就像函数一样。
# 2.封装并不等同于多态。多态可以让用户对不知道的类（或对象类型）的对象进行方法调用，而封装可以不用关心对象是如何创建的，直接使用即可。

# 实例：可以通过函数调用类，并得到结果。
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
stu=Student("jackson",99.5)
def info(stu):
    print("%s的成绩是%.1f分"%(stu.name,stu.score))
info(stu)
# 总结：
# 我们从外部看Student类，只需要知道创建实例需要给出的name和score，如何输出是在Student类的内部定义的，这些数据和逻辑被封装起来，
# 调用很容易，但却不用知道内部实现的细节。
# 封装的另一个好处是可以在Student类增加新的方法，比如get_score(),set_score()方法。

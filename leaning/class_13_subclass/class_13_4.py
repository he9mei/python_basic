#多重继承
# 多重继承，就是有多个基类（父类或超类）。 class 子类名(Base1,Base2,Base3)
# 需要注意圆括号中父类的顺序，若父类中有相同的方法，在子类中使用时未指定，如果方法在子类未找到，python会从父类中从左到右搜索。
# 通过多重继承，一个子类就可以继承多个父类，同时获得多个父类所有非私有功能。

#实例：
class Animal:
    pass
class Mammal(Animal):
    def info(self):
        print("哺乳类...")
class Bird(Animal):
    def info(self):
        print("鸟类...")
class runnable:
    def run(self):
     print("能跑的...")
class flyable:
    def fly(self):
     print("能飞的...")
class Dog(Mammal,runnable):
    pass
dog=Dog()
dog.info()
dog.run()
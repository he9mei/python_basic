#继承
# 1.面向对象带来的好处之一是代码的重用，实现重用的方法之一是通过继承机制。
# 2.在面向对象程序设计中，当我们定义一个class时，可以从某个现有的class继承，定义的新class称为子类(subclass)，
# 而被继承的类称为基类、父类或者超类(base class、SuperClass)。
# 3.继承的语法：class 子类名(基类名)
# python中继承有以下特点：
# （1）在继承中，基类的构造方法不会被自动调用，需要在子类的构造方法中专门调用。
# （2）在调用基类的方法时需要加上基类的类名前缀，并带上self参数。区别在于在类中调用普通函数不需要带self参数。
# （3）在python中，首先查找对应类型的方法，如果在子类中找不到，才到基类中逐个查找。
# 4.继承的最大好处是子类获得了父类全部非私有的功能。
# 5.子类不能继承父类中的私有方法，也不能调用父类的私有方法。
# 6.父类扩展了新的方法，子类可以立即获取父类增加的非私有方法。
# 7.继承可以一级一级继承下来，就好比爷爷到爸爸再到儿子的关系。所有类最终可以追溯到根类object。
# 这些继承关系看上去就像一颗倒着的树。

# 实例1：
# 由于在Animals中定义了非私有的run()方法，
# 因此作为Animals的子类,Dogs和Cats什么方法都没有定义，自动拥有父类中的run()方法。
'''
class Animals:
    def run(self):
        print("animal is running...")
class Dogs(Animals):
    pass
class Cats(Animals):
    def eat(self):  #子类也可有拥有自己的方法
        print("cat is eating...")
dog=Dogs()
cat=Cats()
dog.run()
cat.run()  #子类可以调用父类的方法
cat.eat()  #子类也可以自己的方法
'''
# 实例2：子类不能调用父类的私有方法
class Animals:
    def run(self):
        print("Animal is running...")
    def __run(self):
        print("this is a private method...")
class Dogs(Animals):
    pass
dog=Dogs()
dog.run()
# dog.__run()  #报错





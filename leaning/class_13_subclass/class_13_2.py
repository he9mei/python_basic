#多态
#1.当父类和子类存在相同的方法时，子类的方法会覆盖父类的方法，在代码运行时会调用子类的方法，称之为多态。
#2.多态来自希腊语，意思是有多种形式。多态意味着即使不知道变量所引用的对象类型是什么，也能对对象进行操作，
#多态会根据对象（或类）的不同而表现出不同的行为。
#3.为了更好的理解什么是多态，我们对数据类型再做一点说明。当我们定义一个类时，实际上就定义了一种数据类型。
#定义的数据类型和python自带的数据类型（如str、list、dict）没什么两样。
#我们可以用isinstance()方法判断一个变量是否是某个类型。(也可以用type()函数直接查看数据类型)
#在继承关系中如果一个实例的数据类型是某个子类，那它的数据类型也可以看作是父类，但是反过来就不行。
# 4.很多函数或运算符都是多态的，只要使用多态函数或者运算符，多态就会消失。唯一能够毁掉多态的是使用函数显示的检查类型，
#如type、isinstance函数等。如果有可能就尽量避免这些毁掉多态的方式，重要的是让对象按照我们希望的方式工作，无论它是否为正确的类型或类。

# 实例1：
class Animal:
    def run(self):
        print("animal is running...")
class Dog(Animal):
    def run(self):
        print("dog is running...")
class Cat(Animal):
    pass
dog=Dog()
cat=Cat()
dog.run()
cat.run()

# 实例2-结合实例1：isinstance()判断某个变量是否是某个类型
'''
animal=Animal()
print("dog是否为Dogs类型：",isinstance(dog,Dog))  #True
print("dog是否为Animals类型：",isinstance(dog,Animal))  #True
print("animal是否为Animals类型：",isinstance(animal,Animal))  #True
print("animal是否为Dog类型：",isinstance(animal,Dog))  #False
print(type(dog))  #<class '__main__.Dogs'>
print(type(animal))  #<class '__main__.Animals'>
'''
# 实例3-结合实例1：
# 编写一个函数，这个函数接收一个Animal类型的变量，执行时传入Animal的实例。
def run_two_times(animal):  #此处animal只是一个参数名，实际换成别的也行，并不能确定其类型。
    animal.run()
    animal.run()
run_two_times(Animal())   #传入Animal实例
run_two_times(Dog())   #传入Dog实例
run_two_times(Cat())   #传入Cat实例
# 总结：
# 由于Animal类型有run()方法，因此传入的类型只要是Animal类或者继承自Animal类，都会自动调用实际类型的run()方法。
# 多态的意思是：对于一个变量，我们只需要知道它是Animal类型，无需确切知道它的子类型，就可以放心调用run()方法。具体
# 调用的run()方法作用于Animal、Dog还是Cat对象，由运行时该对象的确切类型决定。
# 多态真正的威力在于：调用方只管调用，不管细节。当我们新增一种Animal的子类时，只要确保run()方法编写正确即可，不管
# 原来的代码是如何调用的。这就是著名的"开闭"原则：对于扩展开放，允许新增Animal子类；对于修改封闭，不需要修改依赖
# Animal的run_two_times()等函数。

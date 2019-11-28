#获取对象信息
# python为我们提供了三种获取对象类型的方法：
# 1.type()函数
# 2.isinstance()函数
# 3.dir()函数

# 实例1：types()函数
# 基本数据类型
'''
a=123      #int
b=9.99     #float
c=(1,2,3)  #tuple
d=[1,2,3]  #list
e={"name":"jackson","age":18}  #dict
f="abc"    #str
print(type(f))
# 函数
print(type(abs))  #<class 'builtin_function_or_method'>
# 类的对象/实例
class Student:
    pass
print(type(Student()))  #<class '__main__.Student'>
# 比较两个变量的类型是否相同
print(type(123)==int)  #True
print(type("abc")==str)  #True
print(type(123)==type("abc"))  #False
# 通过操作可以看到判断基本数据类型可以直接写int、str等。
# 怎么判断一个对象是否是函数呢？需要借助types模块的帮助。
def func():
    pass
print(type(func))  #<class 'function'>
import types  #导入types模块
print(type(func)==types.FunctionType)  #True
'''
# 实例2：isinstance()函数
# 要明确class的继承关系，使用type()很不方便，通过判断class的数据类型确定class的继承关系方便的多。这时候可以使用isinstance()函数。
# isinstance()判断的是一个对象是否为该类型本身，或者是否为该类型继承类的类型。
# 附：能用type()类型判断的基本类型也可以用isinstance()判断。
# isinstance()可以判断一个变量是否为某些类型中的一种。如，isinstance(123,(int,str,list))
class Animal(object):
    pass
class Dog(Animal):
    pass
animal=Animal()
dog=Dog()
print(isinstance(dog,Dog) and isinstance(dog,Animal) and isinstance(dog,object))  #True
print(isinstance(animal,Animal) and isinstance(animal,object))  #True
print(isinstance(animal,Dog))  #False
# 附：判断基本类型也可以
print(isinstance("abc",str))  #True
print(isinstance(123,int))  #True
# 判断是否是某些类型中的一种
print(isinstance(animal,(Animal,Dog,object)))  #True
print(isinstance("abc",(int,str,list)))  #True

# 实例3：dir()函数
# 如果要获得一个对象的所有属性和方法，就可以用dir()函数。
print(dir(abs))  #['__call__', '__class__', '__delattr__'...





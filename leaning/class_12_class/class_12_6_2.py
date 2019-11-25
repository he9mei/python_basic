#python类与对象

# 类里面的方法
# 构造方法/初始化方法-2
# 5.构造方法实例变量的访问权限。
# （1）在类的非构造方法中可以调用构造方法实例变量的属性，调用的方式是self.实例变量名，如self.name
# （2）在类的外部也可以调用，调用方式是-实例名.实例变量名，如st.name;并且可以对其（类的内部属性）进行修改
# （3）内部属性不想被外部访问怎么办？self.__属性名，就会私有变量(private)，只有类内部可以访问，类外部不能访问。
# 私有变量的作用：确保外部代码不能随意修改对象内部的状态，通过访问限制的保护，代码更加安全。
# （4）如何获取私有变量？get_attrs方法
# （5）如果修改私有变量？set_attrs方法
# 在python中，通过定义私有变量和对应的set方法可以帮助我们做参数检查，避免传入无效的参数。
# （6）是否存在私有方法？self.__private_method 私有方法和私有变量类似，不能通过外部调用。

# 实例5-1 调用构造方法实例变量，并在类的外部进行修改
'''
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def info(self):
        print("%s考了%.1f分"%(self.name,self.score))  #在非构造方法调用构造方法的实例变量
st=Student("jackson",99.9)
print("修改之前的分数是：",st.score)
st.info()
st.score=60  #在类的外部修改类内部的实例变量值
print("修改之后的分数是：",st.score)
st.info()
'''
# 实例5-2 构造方法的私有变量，格式是：__变量名
'''
class Student:
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def info(self):
        print("%s考了%.1f分"%(self.__name,self.__score))  #在非构造方法调用构造方法的实例变量
st=Student("jackson",99.9)
# print("修改之前的分数是：",st.__score)  #会报错：没有这个属性。类外部无法访问类内部的私有变量。
st.info()
'''
# 实例5-3
# 类的外部获取私有变量，利用get_attrs
# 类的外部修改私有变量，利用set_attrs
'''
class Student:
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def info(self):
        print("%s考了%.1f分"%(self.__name,self.__score))  #在非构造方法调用构造方法的实例变量
    def get_score(self):
        return self.__score
    def set_score(self,score):
        self.__score=score
st=Student("jackson",99.9)
print("修改之前的分数是：",st.get_score())  #在累的外部访问私有变量，通过get方法
st.info()
st.set_score(60)  #在类的外部修改私有变量，通过set方法
print("修改之后的分数是：",st.get_score())
st.info()
'''
# 实例5-4 通过set做参数检查-输入无效参数
'''
class Student:
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def info(self):
        print("%s考了%.1f分"%(self.__name,self.__score))  #在非构造方法调用构造方法的实例变量
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            print("请输入1到100的数字")
st=Student("jackson",99.9)
print("修改之前的分数是：",st.get_score())  #在累的外部访问私有变量，通过get方法
st.info()
st.set_score(-10)  #在类的外部修改私有变量，通过set方法
print("修改之后的分数是：",st.get_score())
st.info()
'''
# 实例5-5 私有方法
class Student:
    def __init__(self):
        pass
    def __info(self):
        print("---这是一个私有方法---")
    def info(self):
        print("---这是一个公共方法---")
        print("---在公共方法中调用私有方法---")
        self.__info()
st=Student()
st.info()
# st.__info()  #AttributeError: 'Student' object has no attribute '__info'

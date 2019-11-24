#python 条件语句

#一、条件语句有固定的句式和语法
# 1.if 条件表达式：
#      #满足条件表达式（true）要执行的代码块
#2.if 条件表达式：
#     满足条件表达式（true）要执行的代码块
#  else：
#     不满足条件表达式（false）要执行的代码块
#3.if 条件表达式1：
#     代码块A
#  elif 条件表达式2：
#     代码块B
#  else
#     代码块C

#二、条件语句总结：
#1.一组条件语句，只有一个if，可以有0或多个elif，可以有0或多个else
#2.if elif 后面必须加条件表达式，否则会报错
#3.else 后面不能加条件表达式，否则会报错
#4.可以根据不同情况进行分支划分

#三、特殊情况
#1.数字0，代表false；非0，代表true
#2.空字符串、空元组、空列表、空字典，代码false；
# 非空字符串、非空元组、非空列表、非空字典，代表true

# 实例1：
# age=18
# if age>=18:   #比较运算符
#     print("已经成年啦！")

# 实例2：
# age=16
# if age>=18:
#     print("已经成年啦！")
# else:
#     print("还没有成年，好好学习！")

#实例3：
# color="yellow"
# if color=="red":
#     print("红灯停")
# elif color=="green":
#     print("绿灯行")
# elif color=="yellow":
#     print("黄灯等一等")
# else:
#     print("颜色异常！")

#实例4：
# a="hello"
# if "o" in a:  #成员运算符
#     print("'o'在{}里面".format(a))
# else:
#     print("'o'不在{}里面".format(a))

#实例5：
# a=10
# b=20
# if a>=10 and b>=10:  #逻辑运算符
#     print("结果成立！")
# else:
#     print("结果不成立！")

#实例6：
# a=0
# b=1
# if b:
#     print("这是if语句")
# else:
#     print("这是else语句")

#实例7：
# a=""
# b="lemon"
# if a:
#     print("这是if语句")
# else:
#     print("这是else语句")
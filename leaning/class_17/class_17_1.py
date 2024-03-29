# 正则表达式
# 正则表达式是处理字符串强大的工具，拥有独特的语法和独立的处理引擎，效率可能哺乳str自带的方法，但功能十分强大。
# 正则表达式是一个特殊字符序列，能帮助用户检查一个字符串是否与某种模式匹配，从而达成快速检索和替换符合某个模式、规则的文本。
# 正则表达式是匹配字符串的强有力的武器。
# 如判断一个邮箱地址是否合法？先创建一个匹配email邮箱的正则表达式；再用该正则表达式匹配用户的输入从而判断是否合法。

#1.正则表达式基本规则：
# 1.单个字符表示
#（1）特殊字符在正则表达式中的应用
'''
.  -->匹配"\n"之外的任何单个字符。如果要匹配"\n"在内的任意字符，使用'[.\n]'模式
\d -->匹配一个数字字符，等价于[0-9]  \D -->\d取反，即匹配一个非数字字符，等价于[^0-9]
\s -->匹配任意空白字符，包括空格、制表符、换页符等，等价于[\f\n\r\t\v]  \S -->\s取反
\w -->匹配包括下划线的任意单词字符，等价于'[A-Za-z0-9_]'   \W -->\w取反
'''
#（2）字符类咋正则表达式中的应用
'''
[Pp]ython -->匹配"Python"或"python"
rub[ye] -->匹配"ruby"或"rube"
[aeiou] -->匹配aeiou中的任意一个字母
[0-9] -->匹配任意数字，类似于[0123456789]
[a-z] -->匹配任意小写字母
[A-Z] -->匹配任意大写字母
[A-Za-z0-9] -->匹配任意字母数字
[^aeiou] -->取反，匹配除开aeiou以外的所有字符
[^0-9] -->取反，皮皮饿出除了数字以外的所有字符
'''
# 2.字符长度的表示
'''  
*  -->任意个数（包括0个）
+  -->至少1个
？  -->0个或1个
{n}  -->n个
{n,m}  -->n-m个
'''

# 实例匹配类似0915-2525368  \d{4}\-\d{3,8}  备注："-"是特殊字符，需要转义"\-"
# 实例匹配类似0915 2525368  \d{4}\s+\d{3,8}  \s+表示至少一个空白符
# 更复杂的规则：
'''
[a-zA-Z\_][0-9a-zA-Z\_]* -->表示以字母或下划线开头，后接任意个数的数字字母下划线组成的字符串。
[a-zA-Z\_][0-9a-zA-Z\_]{0,19} -->限制了字符个数是1-20
A|B -->用于匹配A或者B,如(P|p)ython可以匹配"Python"和"python"
^ -->表示行的开头，^\d 表示必须以数字开头
$ -->表示行的结束，\d$ 表示必须以数字结尾
'''
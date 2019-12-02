# 正则表达式

#2.re模块
# (1)re.match()函数  尝试从字符串的起始位置匹配一个模式
# re.match(pattern,string,flags=0)
# pattern只匹配的正则表达式；string只要匹配的字符串；flags为标志位，用于控制正则表达式的匹配方式，如是否区分大小写、多行匹配等。
# 如果匹配成功，re.match返回一个匹配的对象；否则返回none。
#实例1
'''
import re
print(re.match("hello","hello python"))  #<re.Match object; span=(0, 5), match='hello'>
print(re.match("python","hello python"))  #None
'''
# (2)re.searchc()函数  扫描整个字符串并返回第一个成功匹配的字符
# re.search(pattern,string,flags=0)
# 实例2
'''
import re
print(re.search("hello","hello python"))  #<re.Match object; span=(0, 5), match='hello'>
print(re.search("python","hello python"))  #<re.Match object; span=(6, 12), match='python'>
'''
# re.match()和re.search()的区别
# re.match()只匹配字符串开始的字符，如果开始的字符不符合正则表达式，匹配就会失败，返回none。
# re.search()匹配整个字符串，直到找到一个匹配的对象，匹配结束还没找到，才会返回none。
#（3）re的group()和groups---了解
import re
print(re.search("hello","hello world,hello python"))   #<re.Match object; span=(0, 5), match='hello'>
print(re.search("hello","hello world,hello python").group())  #hello

# 3.贪婪模式和非贪婪模式
#正则表达式通常用于查找匹配的字符串，python中数量词默认是贪婪的，总是尝试匹配尽可能多的字符；非贪婪模式则正好相反，匹配尽可能少的字符。
# 比如，"ab*"贪婪模式匹配"abbbc"结果为"abbb";"ab*?"非贪婪模式匹配"abbbc"结果为"a"
print(re.match("^\d+0*$","102300").group())  #102300
print(re.match("^(\d+)(0*)$","102300").groups())  #('102300', '')
print(re.match("^(\d+?)(0*)$","102300").groups())  #('1023', '00')

# 4.替换---了解

# 时间日期
# 在python中，与时间处理有关的模块包括time\datetime\calender。
# 在python中，通常用时间戳、格式化的时间字符串、struct_time元组，三种方式表示时间。

# time模块，其内置函数有做时间处理的，也有转换时间格式的。
# 1.time()函数
# time()函数用于返回当前时间的时间戳。（1970年01月01日到现在的时间毫秒数）
import time

print(time.time())  # 执行结果：1575119039.8000484
# 2.localtime([secs])函数
# localtime()函数的作用是格式化时间戳为本地时间。如果secs参数未输入，就以当前时间为主转换标准。
print(time.localtime())
# 执行结果：time.struct_time(tm_year=2019, tm_mon=11, tm_mday=30, tm_hour=21,
# tm_min=3, tm_sec=59, tm_wday=5, tm_yday=334, tm_isdst=0)
# 3.gmtime([secs])函数
# gmtime()函数用于将一个时间戳转换为UTC时区（0时区）的struct_time。默认值是time.time()。
print(time.gmtime())  # 执行结果与2相同
# 4.mktime(t)函数
# mktime()函数用于执行与localtime()和gmtime()相反的操作，接收struct_time对象作为参数，返回
# 用秒数表示时间的浮点数。
print(time.mktime(time.localtime()))  # 执行结果：1575120296.0
# 5.asctime(t)
# asctime()函数用于接收时间元组并返回一个可读的形式。
print(time.asctime(time.localtime()))  # 执行结果：”Sat Nov 30 21:30:27 2019
# 6.ctime([secs])函数
# ctime()函数用于把一个时间戳转化为time.asctime()的形式。
# 如果未指定参数secs或参数为none，就会默认将time.time()作为参数。与asctime(localtime())作用相同。
print(time.ctime())  # 执行结果:Sat Nov 30 21:35:51 2019
# 7.sleep(secs)函数
# sleeep()函数用于推迟调用线程的运行，可通过参数secs指定进程挂起时间。
# print(time.ctime())
# time.sleep(5)
# print(time.ctime())
# 执行结果：
# Sat Nov 30 21:40:19 2019
# Sat Nov 30 21:40:24 2019
# 8.clock()函数
# clock()函数用于以浮点数计算的秒数返回当前cpu时间，用来衡量不同程序的耗时。比time.time()更有用。
# def procedure():
#     time.sleep(2)
# t1 = time.clock()
# procedure()
# print("进程时间：", time.clock() - t1)  #AttributeError: module 'time' has no attribute 'clock'
# 不知道怎么报错了
# 9.strftime(format[,t])函数   时间元组-->可读，格式由format决定
# 10.strptime(string[,format])  指定格式-->时间元组




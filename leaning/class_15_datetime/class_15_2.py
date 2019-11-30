# datetime模块
# datetime是date和time的结合体，包括date和time的所有信息。datetime的功能非常强大，支持0001-9999年。
# datetimme定义了5个类：datetime.date\datetime.time\datetime.datetime\datetime.timedelta(时间间隔)\datetime.tzinfo（与时区相关的信息）
# 其中datetime.datetime类的应用最为普遍。
# 1.today() 表示当前本地时间的datetime对象。
import datetime
print(datetime.datetime.today())  # 2019-11-30 22:30:52.556037
# 2.now([tz]) 返回一个datetime对象。如果提供参数tz就获取tz时区所指的本地时间。
print(datetime.datetime.now())  # 2019-11-30 22:37:37.086060
# 3.datetime.utcnow() 返回一个当前utc时间的datetime对象。
print(datetime.datetime.utcnow())  # 2019-11-30 14:53:00.566047
# 4.fromtimestamp(timestamp[,tz]) #根据时间戳创建一个datetime对象
import time
print(datetime.datetime.fromtimestamp(time.time()))   # 2019-11-30 23:02:48.042927
# 5.utcfromtimestamp(timestamp)
print(datetime.datetime.utcfromtimestamp(time.time()))  # 2019-11-30 15:05:12.328474
# 6.strptime(date_string,format)  将格式字符串转换为datetime对象
dt=datetime.datetime.now()
print(dt.strptime(str(dt), '%Y-%m-%d %H:%M:%S.%f'))
# 7.strftime(format) 格式字符串-->datetime对象
dt=datetime.datetime.now()
print(dt.strptime('%Y-%m-%d %H:%M:%S.%f'))











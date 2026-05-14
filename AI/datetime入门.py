import datetime

print(datetime.datetime.now())   #当前系统时间
print(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))   #格式化输出
print(datetime.datetime.now().strftime("%Y-%m-%d"))
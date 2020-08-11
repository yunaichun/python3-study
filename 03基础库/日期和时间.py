import time
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))


import datetime
print(datetime.datetime.now())
interval = datetime.timedelta(minutes=10)
print(interval)
one_day = datetime.datetime(2018, 5, 27)
interval = datetime.timedelta(days=10)
print(one_day + interval)
# datetime 格式化 https://blog.csdn.net/shomy_liu/article/details/44141483
# 含有毫秒
format_date1 = '%Y-%m-%dT%H:%M:%S.%fZ'
prev_time = datetime.datetime.strptime('2020-06-19T04:05:16.77Z', format_date1)
interval = datetime.timedelta(days=int(0))
modified_time = (prev_time + interval).strftime(format_date1)
print(modified_time)

# 不含有毫秒
format_date2 = '%Y-%m-%dT%H:%M:%SZ'
init_time = datetime.datetime.strptime('2019-07-29T17:57:29Z', format_date2).strftime(format_date2)
now_time = datetime.datetime.now().strftime(format_date2)
print(init_time > now_time)

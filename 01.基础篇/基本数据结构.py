import time
# 一、基础数据类型
# int
print(type(8))
# float
print(type(8.8))
# str
print(type('8.8'))
# bool
print(type(False))

# 二、数据类型转换
print(int('8'))
print(str(123))
print(bool(0))

# 三、网络带宽计算
bandWidth = 100
radio = 8
print(bandWidth/radio)

# 字符串操作
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# 切片操作
print(chinese_zodiac[0:4])
# 负索引
print(chinese_zodiac[-1])
# 索引操作
year = 2018
print(chinese_zodiac[year % 12])
# 成员关系
print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)
# 连接操作
print(chinese_zodiac + 'abcd')
# 重复操作
print(chinese_zodiac * 3)

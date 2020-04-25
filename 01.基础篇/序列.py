# 字符串序列: 记录十二生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
print(chinese_zodiac[0:4])
print(chinese_zodiac[-1])
year = 2018
print(chinese_zodiac[year % 12])

print('狗' in chinese_zodiac) # 成员关系
print('狗' not in chinese_zodiac) # 成员关系
print(chinese_zodiac + 'abcd') # 连接
print(chinese_zodiac * 3) # 重复


# 元组序列: 记录星座(tuple)
zodiac_name = (
    u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
    u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'天蝎座', u'射手座',
)
zodiac_days = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
    (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23), 
)

# 序列的类型和大小比较 <class 'tuple'>
print((1, 20) < (2, 19))
print(type(zodiac_days))

# 计算 2 月 15 日是什么星座
(month, day) = (2, 15)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_name[zodiac_len])


# 序列其他做操
tup = (3, 2, 3, 7, 8, 1)
tup.count(3) # 统计 3 出现的次数
tup.index(7) # 统计 7 的 index
list(reversed(tup)) # reversed() 和 sorted() 同样表示对列表 / 元组进行倒转和排序
sorted(tup) # 但是会返回一个倒转后 或者排好序的新的列表 / 元组
print(sorted(tup)) # list.reverse() 和 list.sort() 分别表示原地倒转列表和排序(注意，元组没有内置的这两个 函数)。

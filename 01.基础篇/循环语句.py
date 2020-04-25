# 循环语句
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
for cz in chinese_zodiac:
    print(cz)

# 遍历 1-12
for i in range(1, 13):
    print(i)

# 字符串替换
for year in range(2000, 2019):
    print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))

# break 和 continue 语句
num = 5
while True:
    num = num + 1
    if (num == 8):
        continue
    if (num > 10):
        break
    print(num)


# 元组序列: 记录星座(tuple)
zodiac_name = (
    u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
    u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'天蝎座', u'射手座',
)
zodiac_days = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
    (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23), 
)
month = int(input('请输入月'))
day = int(input('请输入日期'));
#zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
for zd_num in range(len(zodiac_days)):
    if zodiac_days[zd_num] >= (month, day):
        print(zodiac_name[zd_num])
        break
    elif month == 12 and day > 23:
        print(zodiac_name[0])
        break

n = 0
while zodiac_days[n] < (month, day):
    if month == 12 and day > 23:
        print(zodiac_name[0])
        break
    n += 1
print(zodiac_name[n])

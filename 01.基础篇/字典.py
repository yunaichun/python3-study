d = {'mike': 10, 'lucy': 2, 'ben': 30}
print(d.items())
sorted(d.items(), key = lambda x: x[1], reverse = True)


chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (
    u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
    u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'天蝎座', u'射手座',
)
zodiac_days = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
    (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23), 
)
# 存储生肖数量的字典
cn_name = {}
for i in chinese_zodiac:
    cn_name[i] = 0
# 存储星座数量的字典
z_name = {}
for i in zodiac_name:
    z_name[i] = 0


while True:
    year = int(input('请输入年'))
    month = int(input('请输入月'))
    day = int(input('请输入日期'))
    n = 0
    while zodiac_days[n] < (month, day):
        if month == 12 and day > 23:
            print(zodiac_name[0])
            break
        n += 1
    # 输出生肖
    print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))
    cn_name[chinese_zodiac[year % 12]] += 1
    for each_key in cn_name.keys():
        print('生肖 %s 有 %s 个'%(each_key, cn_name[each_key]))
    # 输出星座
    print(zodiac_name[n])
    z_name[zodiac_name[n]] += 1
    for each_key in z_name.keys():
        print('星座 %s 有 %s 个'%(each_key, z_name[each_key]))

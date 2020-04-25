x = 'abc'
if x == 'abc':
    print('a')
elif x == 'bcd':
    print('b')
else:
    print('c')


# 接收用户输入
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = int(input('请用户输入出生年份'))
print(chinese_zodiac[year % 12])

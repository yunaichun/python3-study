# 从 1 到 10 所有偶数的平方
a_list = []
for i in range(1, 11):
    if i % 2 == 0:
        a_list.append(i*i)
print(a_list)

# 列表推导式
b_list = [i*i for i in range(1, 11) if i % 2 == 0] # 给列表的每一项赋值为 i*i
print(b_list)

# 字典推导式
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
cn_name = {}
for i in chinese_zodiac:
    cn_name[i] = 0
print(cn_name)
zz_name = {i: 0 for i in chinese_zodiac} # 给字典的每一项赋值为 i: 0
print(zz_name)

a_list = ['abc', 'xyz']
a_list.append('X')
a_list.remove('xyz')
print(a_list)
print(type(a_list))

# 列表其他做操
l = [3, 2, 3, 7, 8, 1]
# 统计 3 出现的次数
l.count(3)
# 统计 7 的 index
l.index(7)
# 反转数组
l.reverse()
# 从小到大排序
l.sort()
print(l)

# 列表和元组互相转换
list((1, 2, 3))
tuple([1, 2, 3])

# 嵌套
l = [[1, 2, 3], [4, 5]]

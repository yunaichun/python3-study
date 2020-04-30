######### 浅拷贝
l1 = [[1, 2], (30, 40)]
l2 = list(l1)

l1.append(100) # 列表会引用同一个地址
l1[0].append(3)
print(l1) # [[1, 2, 3], (30, 40), 100]
print(l2) # [[1, 2, 3], (30, 40)]
 
l1[1] += (50, 60) # 元组不可变，所以会重新开一个内存
print(l1) # [[1, 2, 3], (30, 40, 50, 60), 100]
print(l2) # [[1, 2, 3], (30, 40)]


######### 深度拷贝
import copy
l1 = [[1, 2], (30, 40)]
l2 = copy.deepcopy(l1)
l1.append(100)
l1[0].append(3)
 
print(l1) # [[1, 2, 3], (30, 40), 100]
print(l2) # [[1, 2], (30, 40)]


######### 循环引用
x = [1]

x.append(x)
print(x) # [1, [...]]
 
y = copy.deepcopy(x)
print(y) # [1, [...]]

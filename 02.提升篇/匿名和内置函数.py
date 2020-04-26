# lambda 表达式: 匿名函数
def true():return True # 等价于 lambda: True;
def add(a, b):return a+b # 等价于 lambda a,b: a+b
def func(item): return item[1] # 等价于 lambda item: item[1]
adict = {'a': 11, 'b': 22}
for i in adict.items():
    print((lambda item: item[1])(i))

# 内建函数: filter()、map()、reduce()、zip()
a = [1, 2, 3]
b = [4, 5, 6]
print(list(filter(lambda x: x> 2, a)))
print(list(map(lambda x,y: x + y, a, b)))
from functools import reduce
print(reduce(lambda x, y: x+y, a, 1))
for i in zip((1, 2, 3), (4, 5, 6)):
    print(i)
adict = {'a': 11, 'b': 22}
bdict = zip(adict.values(), adict.keys())
print(dict(bdict))

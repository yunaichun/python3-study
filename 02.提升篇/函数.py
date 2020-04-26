# 函数关键字参数
print('abc', end='\n\n')
def func(a, b, c):
    print('a= %s' %a)
    print('b= %s' %b)
    print('c= %s' %c)
func(1, c = 2, b =3)

# 可变函数参数
def howlong(first, *other):
    print(1 + len(other))
howlong(123, 234, 456)

# 函数的变量作用域
var1 = 123
def func():
    # global var1
    var1 = 456
    print(var1)
func()
print(var1)

# 函数的迭代器
list1 = [1, 2, 3]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

# 函数的生成器
def frange(start, end, step):
    x = start
    while x < end:
        yield x
        x += step
for i in frange(10, 20, 0.5):
    print(i)

# lambda 表达式
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

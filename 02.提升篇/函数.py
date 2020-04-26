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

# 闭包
def sum(a):
    def add(b):
        return a+b
    return add
print(sum(1)(2))
def counter(FIRST=0):
    cnt = [FIRST]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one
num1 = counter(5)
print(num1())
print(num1())
def a_line(a, b):
    return lambda x: a * x + b
line1 = a_line(3, 5)
print(line1(10))

# 装饰器
import time
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('函数运行了 %s 秒' %(end_time - start_time))
    return wrapper
@timer
def i_can_sleep():
    time.sleep(1)
i_can_sleep()
# num = timer(i_can_sleep)
# num()
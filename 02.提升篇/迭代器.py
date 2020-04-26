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

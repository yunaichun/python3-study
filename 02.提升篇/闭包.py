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

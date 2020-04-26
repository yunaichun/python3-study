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

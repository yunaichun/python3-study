# 不带参数装饰器
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
# 装饰器等价于如下写法
# num = timer(i_can_sleep)
# num()


# 带参数装饰器
def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s %s' %(argv, func.__name__))
            func(a, b)
            print('end')
        return nei
    return tips
@new_tips('add')
def add(a, b):
    print(a+b)
add(4, 5)
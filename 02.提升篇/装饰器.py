# 一、不带参数装饰器
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


# 二、带参数装饰器
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


# 三、类装饰器
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
 
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)

@Count
def example():
    print("hello world")

example()
example()


# 四、应用-身份认证登录拦截、日志记录、输入合理性检查
import functools
def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request): # 如果用户处于登录状态
            return func(*args, **kwargs) # 执行函数 post_comment() 
        else:
            raise Exception('Authentication failed')
    return wrapper

@authenticate
def post_comment(request):
    print(111)

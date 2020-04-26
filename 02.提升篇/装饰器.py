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
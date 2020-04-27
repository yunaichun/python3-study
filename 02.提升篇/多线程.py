import threading
import time
from threading import current_thread
def myThread(arg1, arg2):
    print(current_thread().getName(), 'start')
    print('%s %s' %(arg1, arg2))
    time.sleep(1)
    print(current_thread().getName(), 'stop')
for i in range(1, 6, 1):
    # 定义多线程
    t1 = threading.Thread(target = myThread, args = (i, i + 1))
    # 开启线程，实际是执行 threading.Thread 的 run 方法
    t1.start()
    # 执行完成子线程之后才执行主线程 - t1.join()
# 打印主线程
print(current_thread().getName(), 'end')


##### 改进版 #####
class Mythread(threading.Thread):
    def run(self):
        # return super().run()
        print(current_thread().getName(), 'start')
        time.sleep(1)
        print(current_thread().getName(), 'stop')
for i in range(1, 6, 1):
    t1 = Mythread()
    t1.start()
    t1.join()
print(current_thread().getName(), 'end')

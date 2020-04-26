# 模块导入后重命名
import time as t
print(t.time())

# 引入指定方法[不太推荐]
from time import time,sleep
print(time())

# 引入自定义模块
import 闭包
print(闭包.sum(1)(2))

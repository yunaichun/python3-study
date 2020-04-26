# try...catch...捕获异常
file = open('name.txt')
try:
    for line in file.readlines():
        print(line)
except Exception as e:
    print(e)
finally:
    fd.close()

# 上下文管理器 with 可以不用写 try...catch...
with open('name.txt') as file:
    for line in file.readlines():
        print(line)

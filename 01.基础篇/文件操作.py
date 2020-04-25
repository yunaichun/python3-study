# 写入文件
file1 = open('name.txt', 'w')
file1.write('诸葛亮')
file1.close()

# 读取文件
file2 = open('name.txt', 'r')
print(file2.read())
file2.close()

# 文件追加
file3 = open('name.txt', 'a')
file3.write('诸葛亮2')
file3.close()

# 读取一行
file4 = open('name.txt', 'r')
print(file4.readline())

逐行读取
file5 = open('name.txt', 'r')
for line in file5.readlines():
    print(line)


file6 = open('name.txt', 'r')
# 文件行的指针
print('当前文件的位置: %s' %file6.tell())
# 读取第一行是 3, 读取第一行是 1
file6.read(1)
print('当前文件的位置: %s' %file6.tell())
# 回到初始指针【第一个参数代表偏移位置；第二个参数: 0代表从文件开头位置偏移，1代表从当前位置偏移，2代表文件结尾位置偏移】
file6.seek(0, 0)
print('当前文件的位置: %s' %file6.tell())
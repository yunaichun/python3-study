import re
p = re.compile('ca*t')
print(p.match('caaaat'))


# 匹配任意字符 .
p = re.compile('...')
print(p.match('cat'))
# 开头和结尾 ^ $


# 出现0次以及以上 *
# 出现1次以及以上 +
# 出现0次或1次 ?
# 出现指定次数 {m}
# 出现指定次数范围 {m,n}


# 匹配任意一个十进制数字 \d  等价于 [0-9]+   【\D 等价于 [^0-9]+】
# 匹配任意一个不可见原子 \s  
# 匹配任意一个数字、字母、下划线 \w
# 匹配其中一个字符 []
# 匹配2个或多个分支选择 |
# 分组 ()
print('\nx\n')
#'r'是防止字符转义的, 如果路径中出现'\t'的话: 
# 1、不加r的话\t就会被转义；2、而加了'r'之后'\t'就能保留原有的样子
print(r'\nx\n')
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2018-5-10').group(1))
print(p.match('2018-5-10').groups())
(year, month, day) = p.match('2018-5-10').groups()
print(year, month, day)
# 搜索匹配
print(p.search('aaaa2018-5-10bbbb'))
# 替换匹配
phone = '123-456-789 # 这是电话号码'
p2 = re.sub(r'#.*', '', phone)
print (p2)


# 匹配空行 ^$
# 不使用贪婪模式 .*? 【匹配更少的】

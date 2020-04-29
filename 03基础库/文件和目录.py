import os
# from os import path
print(os.path.abspath('.'))
print(os.path.exists('/Users'))
print(os.path.isfile('/Users'))
print(os.path.isdir('/Users'))
print(os.path.join('/Users/', 'a'))


from pathlib import Path
p = Path('.')
print(p.resolve()) # 等价于 print(os.path.abspath('.'))
print(p.exists())
print(p.is_file())
print(p.is_dir())
# 加持功能
q = Path('/Users/yunaichun/Downloads/a/b')
# q.parents=True 代表的是父级目录不存在则自动创建
Path.mkdir(q, parents=True)

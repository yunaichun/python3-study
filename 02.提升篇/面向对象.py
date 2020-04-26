# 面向过程适合机器, 面向对象适合人类思维
class Player():
    def __init__(self, name, hp, occu):
        super().__init__()
        self.name = name
        self.hp = hp
        self.__occu = occu # __ 表示属性不可被修改
    # 定义一个方法
    def print_role(self):
        print('%s %s %s' %(self.name, self.hp, self.__occu))
    def updateName(self, newName):
        self.name = newName
user1 = Player('tom', 100, 'war')
user2 = Player('jerry', 90, 'master')
user1.print_role()
user2.print_role()

# 继承、多态
class Monster():
    '定义怪物类'
    def __init__(self, hp = 100):
        super().__init__()
        self.hp = hp
    def run(self):
        print('移动到某个位置')
a1 = Monster(200)
a1.run()
class Animals(Monster):
    '普通怪物'
    # pass
    def __init__(self, hp = 10):
        # 直接继承父类的实例属性，不用写 self.hp = hp
        super().__init__(hp)
a2 = Animals(20)
a2.run()
print('a1 类型 %s' %type(a1))
print('a2 类型 %s' %type(a2))
print('a2 是不是 Monster 子类:  %s' %isinstance(a2, Monster))
print('a2 是不是 object 子类:  %s' %isinstance(a2, object))

# with 打开文件异常处理
class TestWith():
    def __enter__(self):
        print('run')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常结束')
        else:
            print('has error %s' %exc_tb)
with TestWith():
    print('Test is runing')
    raise NameError('testNameError')


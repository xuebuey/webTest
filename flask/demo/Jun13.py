#函数
#print()
#a = 2.23232323
#print(round(a,3))  #2.23
'''
函数内部执行了return , 后面的代码不会执行
import sys
sys.setrecursionlimit(29)
def add(x, y):
    print(x + y)
    result = x-y
    return result

a = add(2,3)
print(a)
'''

'''
提高阅读性，接收函数结果方式，用名称代替damage[0]使接受的参数简单明了
def damage(skill1, skill2):
    damage1 = skill1+skill2
    damage2 = skill1*skill2
    #return {'s':damage1,'f':damage2}
    return damage1,damage2

skill1_damages1, skill1_damages2 = damage(2,3)
print(skill1_damages1)
print(skill1_damages2)
print(type(skill1_damages2))
'''

'''
#序列解包
a = 1, 2, 3
print(type(a))
c,d,e = a
print(c)
print(type(c))
'''
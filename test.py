
'''
//hashlib
import hashlib

a= hashlib.new('md5', b'what you are fucking about').hexdigest()
print(a)
'''

'''
def func():
    yield 1
    yield 2
    yield 3

f=func()
print(f.send(4))
'''

'''
//map
def f(x,y):return [x,y]

l1=[1,2,3,4,5,6]
l2=['one','two','three','four','five','six']

n=list(map(f,l1,l2))
print(n)
'''

'''
//reduce
from functools import reduce
def add(x, y) :            # 两数相加
     return x + y

n=reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5

print(n)
'''

'''
//filter
def f1(x):
    if x > 20:
        return True
    else:
        return False

l1 = [ 1, 2, 3, 42, 67, 16 ]
f=filter( f1, l1)
result=list(f)
print(result)
'''



























































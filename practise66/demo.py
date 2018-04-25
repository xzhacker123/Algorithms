# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 16:47
# @Author  : Alex.xu
# @File    : demo.py
# @Software: PyCharm
import copy
import pprint
a = [i for i in range(0, 10, 3)]
a = []
for i in range(10):
    b = []
    for j in range(15):
        b.append(i*2+j*(i+1)*2)
    a.append(copy.copy(b))

for i in a:
    print i
def p1(a, k, i=0, j=0):
    t1 = i
    t2 = j
    try:
        for b in range(len(a[0])-3):
            if k > a[i][j] and k <a[i+1][j+1]:
                pass
                p1(a, k, i, t2)#横坐标
                p1(a, k, t1, j)#纵坐标
            elif k == a[i][j]:
                return i,j
            i += 1
            j += 1
    except:
        pass
v = p1(a, 638)
print v
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：输出9*9口诀。

'''
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print '%d * %d = %d' % (i,j,result)
    print '' # 每计算完一个数换行
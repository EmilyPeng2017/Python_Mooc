#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
变量可以指向函数，函数名其实就是指向函数的变量
'''
# print abs(-111)
'''
高阶函数：能够接收函数作为参数的函数
demo:接收abs函数作为参数，定义一个函数，接收x,y,f三个参数，其中x.y是普通的数，f是函数
'''
def add(x,y,f):
    return f(x)+f(y)

print add(-1,-22,abs)
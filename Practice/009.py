#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：要求输出国际象棋棋盘。
1.程序分析：用i控制行，j来控制列，根据i+j的和的变化来控制输出黑方格，还是白方格。
'''
# import sys
# for i in range(8):
#     for j in range(8):
#         if(i + j) % 2 == 0:
#             sys.stdout.write(chr(219))
#             sys.stdout.write(chr(219))
#         else:
#             sys.stdout.write(' ')
#     print ''
import sys
sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
print ''

for i in range(1,11):
    for j in range(1,i):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
    print ''

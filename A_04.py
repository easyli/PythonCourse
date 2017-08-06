#!/usr/bin/python3

'''
温度转换程序
'''

val = input("请输入温度表示符的温度值(如 : 32C)")
if val[-1] in ['C', 'c']:
    f = 1.8 * float(val[0:-1]) + 32
    print("转换后的温度为: % 0.2fF" %f)
elif val[-1] in ['F', 'f']:
    c = (float(val[0:-1]) - 32) / 1.8
    print("转换后的温度为: % 0.2fc" %c)
else:
    print("输入有误")
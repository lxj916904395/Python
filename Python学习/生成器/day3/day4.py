#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#循坏结构


# # 用for循环实现1~100求和
# sum = 0
# for x in range(101):
# 	sum += x
# print(sum)


# # 用for循环实现1~100之间的偶数求和
# sum = 0
# for x in range(2, 101, 2):
# 	sum += x
# print(sum)


# import random
# answer = random.randint(1,100)
# count = 0
# while True:
#     count+=1
#     num = int(input('请输入：'))
#     if num < answer:
#         print('大一点')
#     elif num > answer:
#         print('小一点')
#     else:
#         print('答对了')
#         break
#
# print('总共猜了%d次' % count)
# if count >7:
#     print('你的智商严重不足，请重修九年义务教育')


# #乘法口诀
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d * %d = %d' % (j,i,i*j),end='\t')
#     print('\n')


# #判断素数
# from math import  sqrt
# num = int(input('输入一个整数：'))
# end = int(sqrt(num))
#
# is_prim = True
#
# for x in range(2,end+1):
#     if num % x == 0:
#         is_prim = False
# if is_prim and num != 1:
#     print('%d是素数' % num)
# else :
#     print('%dbu是素数' % num)


# str1 = 'hello, world!'
# # 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(60, '*'))
#
# list2 = ['hello'] * 5
# print(list2)
#
# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# # 循环遍历列表元素
# for fruit in fruits:
#     print(fruit.title(), end=' ')


# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
#
# print(list1)
# print()
# print(list2)

# t = ('骆昊', 38, True, '四川成都')
# print(t)
# t = ('王大锤', 20, True, '云南昆明')
# print(t)



#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 分支结构 （有多种情况、只有一种情况被执行，即 if else）
import  getpass

# name = input('请输入用户名：')
# password = input('请输入密码：')
# # password = getpass.getpass('请输入密码:')
#
# if name == 'admin' and password == '123456':
#     print('用户验证通过')
# else:
#     print('用户验证失败')`


# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 == %f 厘米' % (value, value*2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 == %f英寸' % (value,value/2.54))
# else:
#     print('请输入有效单位')



# from  random import  randint
#
# face = randint(1,6)
# if face == 1:
#     result = '压抑'
# elif face == 2:
#     result = '心凉'
# elif face == 3:
#     result = '郁闷'
# else:
#     result = '滚'
# print(result)


# import math
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a+b > c and a+c > b and b+c > a:
#     print('周长:%d' % (a+b+c))
#     p = (a+b+c)/2
#     area = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print('面积:%f' % (area))
# else :
#     print('不能构成三角形')


salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 3500
if diff <= 0:
	rate = 0
	deduction = 0
elif diff < 1500:
	rate = 0.03
	deduction = 0
elif diff < 4500:
	rate = 0.1
	deduction = 105
elif diff < 9000:
	rate = 0.2
	deduction = 555
elif diff < 35000:
	rate = 0.25
	deduction = 1005
elif diff < 55000:
	rate = 0.3
	deduction = 2755
elif diff < 80000:
	rate = 0.35
	deduction = 5505
else:
	rate = 0.45
	deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))
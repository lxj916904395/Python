# def normalize(name):
#     h = name[:1]
#     o = name[1:]
#     return h.upper()+o.lower()
#
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

from functools import  reduce
#
# def prod1(x,y):
#     return  x*y
#
# def prod(L):
#     return reduce(prod1,L)

# def str2float(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
# def num2(x,y):
#     return x*10+y
#
# l = reduce(num2,map(str2float,'123.456'))
# print(l)

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[1]
# print(sorted(L,key=by_name))


# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#
#     return sum
#
# f = lazy_sum(1,2,3)
#
# print(f())

# def count(*args):
#     fs = []
#     for i in args:
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1,f2,f3 = count(1,2,3)
# print(f1())
# print(f2())
# print(f3())


# f = float(input('请输入华氏温度：'))
# c = (f-32)/1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f,c))


# import  math
#
# radius = float(input('请输入圆的半径：'))
# zhouchang = 2*radius*math.pi
# mianji = math.pi*radius*radius
# print('周长：%.2f' % zhouchang)
# print('面积：%.2f' % mianji)

year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print("闰年：%d" % is_leap)

#!/usr/bin/env python 
# -*- coding:utf-8 -*-



import os
import time


# def main():
#     content = '北京欢迎你为你开天辟地…………流动的血液充满着朝气。。。。。'
#     while True:
#         # os.system('clear')
#         print(content)
#         time.sleep(2)
#         content = content[1:] + content[0]


def file():
    filename = str(input('请输入文件名:'))
    pos = filename.find('.')

    if 0 < pos < len(filename) - 1:
        print('后缀:%s' % filename[pos + 1:])
    else:
        file()

# //找最大的两个数
def findMax(x):
    x1,x2 = (x[0],x[1]) if x[0] > x[1] else (x[1],x[0])

    for num in range(2,len(x)):
        if x[num] > x1:
            x2 = x1
            x1 = x[num]

        elif x[num] > x2:
            x2 = x[num]

    print(x1,x2)


# 计算指定的年月日是这一年的第几天
def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
def which_day(year,month,day):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]

    totol = 0
    for index in range(month-1):
        totol += days_of_month[index]
    print('第%d天' % (totol + day))


# 杨辉三角
# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()

# 约瑟夫环问题
def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')




if __name__ == '__main__':
    # findMax([1,13,4,6,2,15])
    # year = int(input('请输入年份：'))
    # month = int(input('请输入月份：'))
    # day = int(input('请输入号数：'))
    # which_day(year,month,day)
    main()
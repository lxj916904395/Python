#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

"""自定义枚举类"""
# unique ，防止出现重复的值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


"""自定义枚举类"""
class Gender(Enum):
    Male = 0,
    Female = 1,


class Student:
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender


def main():
    # value属性则是自动赋给成员的int常量，默认从1开始计数。
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    for name, member in Weekday.__members__.items():
        print(name, '=>', member, ',', member.value)

    s = Student('lxj', Gender.Male)
    print(s)

if __name__ == '__main__':
    main()
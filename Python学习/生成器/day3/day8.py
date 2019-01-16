#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep


class Student(object):
    # 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，
    # 如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
    # 单下划线，表示属性、方法是受保护的，单下划线开头的属性和方法外界仍然是可以访问的

    def __init__(self, name, age, sex):
        self.__name = name
        self.age = age
        self._sex = sex

    # 私有方法
    def __study(self, classname):
        print('%s正在学习%s', self.__name, classname)

    # 开放方法
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.__name)
        else:
            print('%s正在观看岛国爱情动作片.' % self.__name)


class Test:
    # 设置私有属性
    def __init__(self, foo):
        self.__foo = foo

    # 设置私有方法
    def __bar(self):
        print('我是私有方法 __bar')


# 时钟
class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def __str__(self):
        """"显示时间"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    lxj = Student('wkl', 20,'男')
    lxj.watch_av()

    # 调用对象私有方法
    test = Test('ll')
    test._Test__bar()

    clock = Clock(23, 59, 58)
    while True:
        print(clock)
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()

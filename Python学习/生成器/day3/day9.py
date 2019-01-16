#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from math import sqrt
from abc import ABCMeta, abstractmethod

""""修饰器"""""

class Person:

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_sex')

    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

"""继承"""

# 学生类继承Person类
class Student(Person):

    def classid(self):
        return 1008611


"""静态方法"""

class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 标识静态方法
    @staticmethod
    def is_vaible(a, b, c):
        return a+b > c and a+c > b and b+c > a

    # 标识类方法
    @classmethod
    def classis_vaible(cls):
        # 创建对象并返回
        return cls(5, 6, 7)


    def area(self):
        p = (self._a+self._b+self._c)/2
        return sqrt(p*(p-self._a)*(p-self._c)*(p-self._b))


"""继承、多态"""
# 抽象类,不能够实例化，只能调用子类的实例
# abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，
# 如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象)
class Pet(metaclass=ABCMeta):
    # 抽象方法
    @abstractmethod
    def make_voice(self):
        print('叫啊')

class Cat(Pet):
    def make_voice(self):
        print('瞄、、瞄')

class Dog(Pet):
    def make_voice(self):
        print('汪、、汪')


def main():
    p = Person('lxj', 20, 'man')
    p.age = 18
    print('%s 年纪:%d' % (p.name, p.age))
    p.play()

    # a, b, c = 12, 12, 12
    # if Triangle.is_vaible(a, b, c):
    #     t = Triangle(a, b, c)
    #
    #     # 两种不同方法调用对象方法
    #     # print('面积:%.f' % (t.area()))
    #     print('面积:%.f' % (Triangle.area(t)))
    #
    # else:
    #     print('无法构成三角形')

    t1 = Triangle.classis_vaible()
    t1.area()
    print('面积:%.f' % (Triangle.area(t1)))


    Dog().make_voice()
    Cat().make_voice()




if __name__ == '__main__':
    main()

#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    # 当前准备创建的类的对象；
    #
    # 类的名字；
    #
    # 类继承的父类集合；
    #
    # 类的方法集合。
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 添加关键字参数metaclass时，
# Python解释器会在创建MyList时，要通过ListMetaclass.__new__()来创建，
class MyList(list, metaclass=ListMetaclass):
    pass


def main():
    l = MyList()
    l.add(1)
    print(l)

if __name__ == '__main__':
    main()
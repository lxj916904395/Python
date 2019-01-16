#!/usr/bin/env python 
# -*- coding:utf-8 -*-


# 先定义函数
def fn(self, name='world'):
    print('Hello,%s' % name)


def main():
    # 创建Hello class
    # type()函数依次传入3个参数：
    #
    # class的名称；
    # 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    # class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
    Hello = type('Hello', (object,), dict(hello=fn))

    # 创建实例
    h = Hello()
    # 调用实例方法
    h.hello('Python')






if __name__ == '__main__':
    main()
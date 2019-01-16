#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from threading import Thread,Lock
from time import sleep

class Account:
    def __init__(self):
        self._blance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        # 先获取锁才能执行后续的代码

        try:
            new_blance = self._blance + money
            sleep(0.01)
            self._blance = new_blance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def blance(self):
        return self._blance


class AddThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)



def main():

    account = Account()
    threads = []

    for _ in range(100):
        t = AddThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('账户余额为: ￥%d元' % account._blance)


if __name__ == '__main__':
    main()

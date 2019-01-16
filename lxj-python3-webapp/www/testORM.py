#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import asyncio, sys
import www.lxjorm
from www.Models import User

async def test(loop):
    await www.lxjorm.create_pool(loop, user='root', password='12345678', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='123456', image='about.blank')
    await u.save()

async def findAll():
    uers = await User.findAll()
    print(uers)



if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait([test(loop)]))
    # loop.close()
    # if loop.is_closed():
    #     sys.exit(0)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(findAll())
    loop.close()
    if loop.is_closed():
        sys.exit(0)


#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import asyncio

async def hello():
    print('你哈1')
    r = await asyncio.sleep(1)
    print('11')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()
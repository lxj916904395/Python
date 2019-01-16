#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import psutil

print('CPU逻辑数量===', psutil.cpu_count())

print('CPU物理核心===', psutil.cpu_count(logical=False))

print('统计CPU的用户／系统／空闲时间===', psutil.cpu_times())

for x in range(2):
    print('CPU使用率===', psutil.cpu_percent(interval=1, percpu=True))

print('物理内存===', psutil.virtual_memory())

print('交换内存===', psutil.swap_memory())

print('获取网络读写字节／包的个数===', psutil.net_io_counters())

print('获取网络接口信息===', psutil.net_if_addrs())

print('获取网络接口状态===', psutil.net_if_stats())

# print('当前网络连接信息===', psutil.net_connections())

print('所有进程ID===', list(psutil.pids()))

# # 获取指定进程
# progress = psutil.Process(5532)
# print('指定进程===', progress.name)


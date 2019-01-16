#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta, timezone

"""获取当前时间"""
now = datetime.now()
print('当前时间:%s,时间戳:%s' % (now, now.timestamp()))

"构造时间"
c = datetime(2018, 11, 15, 15, 21)
print('我是构造的时间:%s,时间戳:%s' % (c, c.timestamp()))


"""时间戳构造时间"""
p = 1872222222
t = datetime.fromtimestamp(p)
print('我是来自时间戳的时间:%s' % t)

"""UTC 标准时间"""
print('我是UTC时间:%s' % datetime.utcfromtimestamp(p))


"""字符串转换时间"""
str_time = '2018-11-15 15:25:12'
time = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
print('字符串转时间：%s' % time)


"""时间转换字符串"""
print("现在时间:%s" % now.strftime('%Y-%m-%d %H:%M ,%a,%b')) #a:星期，b:月份


"""时间加减"""
# 当前时间往后10小时
time10 = now + timedelta(hours=10)
print("当前时间:%s,往后10小时:%s" % (now, time10))

time2 = now + timedelta(days=2, hours=11)
print("当前时间:%s,往后2天再加上11小时:%s" % (now, time2))


# 当前时间往前24小时
yestoday = now - timedelta(days=1)
print("当前时间:%s,昨天的当前时间:%s" % (now, yestoday))


"""时区转换"""
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)# tzinfo ：时区属性

# 将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))


print("UTC时间:%s, 北京时间：%s" % (utc_dt, bj_dt))

# 0时区十几年转换为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# 北京时间转换为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))

print("UTC转东京时间:%s, 北京时间转东京时间：%s" % (tokyo_dt, tokyo_dt2))
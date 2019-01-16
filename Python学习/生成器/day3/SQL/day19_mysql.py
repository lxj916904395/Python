#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import mysql.connector

# 初始化链接
# user:mysql登录名
# password：登录密码
# database：连接的数据库
conn = mysql.connector.connect(user='root',
                               password='lxj4522241991',
                               database='mytest')


# 游标
cursor = conn.cursor()

# 创建user表
cursor.execute('create table user (id varchar(20) primary key ,name varchar(20) )')

# 插入数据
cursor.execute('insert into user (id, name) values(%s, %s)', ['1', 'lxj'])

# 影响行数
print(cursor.rowcount)

# 提交事务
conn.commit()

# 查询user
cursor.execute('select * from user ')

# 查询结果
vaulus = cursor.fetchall()

print(vaulus)


# 关闭连接
cursor.close()
conn.close()







# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class BiqugePipeline(object):
    def process_item(self, item, spider):

        name = item['bookname']
        body = item['body']
        title = item['title']
        order_id = item['order_id']


        # 链接数据库
        conn = pymysql.connect(

            host='localhost',
            user='root',
            passwd='12345678',
            db='bqgxiaoshuo',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

        try:
            with conn.cursor() as cursor:
                print('插入')
                sql1 = 'Create Table If Not Exists %s(id int,zjm varchar(20),body text)' % name
                sql = 'Insert into %s values (%d ,\'%s\',\'%s\')' % (
                    name, order_id, title, body)
                cursor.execute(sql1)
                cursor.execute(sql)


            conn.commit()

        finally:
            conn.close()

            return item
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os, requests, json, codecs, pymysql

class WeatherPipeline(object):
    def process_item(self, item, spider):
        print('执行：WeatherPipeline')


        '''
        处理每一个从SZtianqi传过来的
        item
        '''

        # 获取当前工作目录
        base_dir = os.getcwd()
        # 文件存在data目录下的weather.txt文件内
        fiename = base_dir + '/weather/data/weather.txt'
        # print(fiename)
        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n\n')

        # # 下载图片
        # with open(base_dir + '/weather/data/' + item['date'] + '.png', 'wb') as f:
        #     f.write(requests.get(item['img']).content)

        return item


class W2json(object):
    def process_item(self, item, spider):
        print('执行：W2json')

        '''
        讲爬取的信息保存到json
        方便其他程序员调用
        '''
        base_dir = os.getcwd()
        filename = base_dir+'/weather/data/weather.json'
        # print('写入json%s' % filename)

        # 打开json文件，向里面以dumps的方式吸入数据
        # 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如:“/xe15”
        with open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            f.write(line)

        return item

class W2mysql(object):
    def process_item(self, item, spider):
        print('执行：W2mysql')
        '''
        将爬取的信息保存到mysql
        '''

        date = item['date']
        week = item['week']
        temperature = item['temperature']
        weather = ''
        wind = item['wind']
        img = item['img']

        # 将item里的数据拿出来
        # date = item['date']
        # week = item['week']
        # weather = item['weather']
        # wind = item['wind']
        # img = item['img']

        # 和本地的scrapyDB数据库建立连接
        connection = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',        # 自己的mysql用户名
            passwd='12345678',  # 自己的密码
            db='scrapyDB',      # 数据库的名字
            charset='utf8mb4',     # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # 创建更新值的sql语句

                sql1 = 'Create Table If Not Exists WEATHER(date varchar(50), week varchar(25),temperature varchar (25),weather varchar (25),wind varchar (25),img varchar (50))'

                sql = """INSERT INTO WEATHER(date,week,temperature,weather,wind,img)
                        VALUES (%s, %s,%s,%s,%s,%s)"""
                # print('数据:%s, %s, %s, %s' % (date, img, weather, week))
                # 执行sql语句
                # excute 的第二个参数可以将sql缺省语句补全，一般以元组的格式
                cursor.execute(sql1)
                cursor.execute(sql, (date, week, temperature, weather, wind, img))

            # 提交本次插入的记录
            connection.commit()

        finally:
            # 关闭连接
            connection.close()

        return item
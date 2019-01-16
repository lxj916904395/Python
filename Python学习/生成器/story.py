#!/usr/bin/env python
#coding=utf-8
import urllib
from urllib import request, parse
import re
import ssl
import json

webroot = 'http://www.xuanshu.com'
context = ssl._create_unverified_context()


def requestPage():
    for page in range(20, 220):
        print('正在下载第' + str(page) + '页小说')
        url = 'http://www.xuanshu.com/soft/sort02/index_' + str(page) + '.html'

        req = request.Request(url)
        # 添加请求头
        req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')

        with request.urlopen(req, context=context) as f:
            print('result:', f.status, f.reason)
            data = f.read()
            json_str = data.decode('utf-8')
            print(json_str)
            # print html
            html = json_str

            pattern = re.compile(
                u'<li>.*?<div class="s">.*?target="_blank">(.*?)</a><br />大小：(.*?)<br>.*?</em><br>更新：(.*?)</div>.*?<a href="(.*?)"><img.*?>(.*?)</a>.*?<div class="u">(.*?)</div>',
                re.S)
            items = re.findall(pattern, html)
            # print items
            downloadDetail(items)

def downloadDetail(items):
    for item in items:
        try:
            book_auther = item[0].encode('gbk')
            book_size = item[1].encode('gbk')
            book_updatetime = item[2].encode('gbk')
            book_link = item[3].encode('gbk')
            book_name = item[4].encode('gbk')
            book_note = item[5].encode('gbk')
            book_link = str(book_link.decode('utf-8'))
            book_full_link = webroot + book_link   # 构建书的绝对地址

            req = request.Request(book_full_link)
            # 添加请求头
            req.add_header('User-Agent',
                           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')

            with request.urlopen(req, context=context) as f:

                data = f.read()
                html = data.decode('utf-8')
                pattern = re.compile('<a class="downButton.*?<a class="downButton" href=\'(.*?)\'.*?Txt.*?</a>', re.S)
                down_link = re.findall(pattern, html)[0]

                req1 = request.Request(down_link)
                # 添加请求头
                req1.add_header('User-Agent',
                               'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')

                with request.urlopen(req1, context=context) as file:
                    book_name = book_name.decode('gb2312')
                    data = file.read()
                    html = data.decode('utf-8')
                    print('写入小说:'+book_name+'/'+html)

                    fp = open('./boos/'+book_name + '.txt', 'w')

                    fp.write(file.read().decode('utf-8'))
                    fp.close()

        except request.HTTPError as e:
            print('出错'+e.reason)

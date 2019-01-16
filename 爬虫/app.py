#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re




def getHntml(url):
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = ('utf8')
    # print(r.text)
    return r.text


def get_content(url):
    url_list = []

    html = getHntml(url)
    soup = BeautifulSoup(html, 'lxml')
    category_list = soup.find_all('div', class_='ndex_toplist mright mbottom')
    history_finished_list = soup.find_all(
        'div', class_='index_toplist mbottom')

    for cate in category_list:
        name = cate.find('div', class_='toptab').span.string
        with open('novel_list.csv', 'a+') as f:
            f.write("\n小说种类：{} \n".format(name))

        # 我们直接通过style属性来定位总排行榜
        general_list = cate.find(style='display: block;')
        # 找到全部的小说名字，发现他们全部都包含在li标签之中
        book_list = general_list.find_all('li')
        # 循环遍历出每一个小说的的名字，以及链接
        for book in book_list:
            link = 'http://www.qu.la/' + book.a['href']
            title = book.a['title']
            # 我们将所有文章的url地址保存在一个列表变量里
            url_list.append(link)
            # 这里使用a模式，防止清空文件
            with open('novel_list.csv', 'a') as f:
                f.write("小说名：{:<} \t 小说地址：{:<} \n".format(title, link))

    for cate in history_finished_list:
        name = cate.find('div', class_='toptab').span.string
        with open('novel_list.csv', 'a') as f:
            f.write("\n小说种类：{} \n".format(name))

        general_list = cate.find(style='display: block;')
        book_list = general_list.find_all('li')
        for book in book_list:
            link = 'http://www.qu.la/' + book.a['href']
            title = book.a['title']
            url_list.append(link)
            with open('novel_list.csv', 'a') as f:
                f.write("小说名：{:<} \t 小说地址：{:<} \n".format(title, link))

    return url_list


def main():
    url = 'http://www.qu.la/paihangbang/'
    list = get_content(url)
    for x in list:
        print(x)


if __name__ == '__main__':
    main()


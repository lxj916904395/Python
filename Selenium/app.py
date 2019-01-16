#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver

import os, requests

base_url = './resources/'

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def save_pic(filename, url):
    conten = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(conten.content)

def get_inf(index_url):
    url_list = []

    broswer = webdriver.Chrome()
    """请求目标链接"""
    broswer.get(index_url)

    """标题"""
    title = broswer.title.split(',')[0]


    # 创建文件
    mkdir(base_url+title)

    # 找到漫画章节，注意，漫画可能会有多种篇章
    # 例如番外，正文，短片等等
    comics_lists = broswer.find_elements_by_class_name('comic_Serial_list')

    # 寻找、正文等
    for part in comics_lists:
        # 找到包裹链接的links
        links = part.find_elements_by_tag_name('a')
        # 找到每个单独的章节链接
        for link in links:
            url_list.append(link.get_attribute('href'))

    # 关闭浏览器
    broswer.quit()

    Comics = dict(name=title, urls=url_list)

    return Comics


def get_pic(Comics):
    list = Comics['urls']
    name = Comics['name']

    browser = webdriver.Chrome()

    for url in list:
        browser.get(url)
        browser.implicitly_wait(3)

        # 创建章节目录
        dirname = base_url + name + '/' + browser.title.split('-')[1]
        mkdir(dirname)

        # 找到该漫画一共有多少页
        pageNum = len(browser.find_elements_by_tag_name('option'))
         # 找到下一页的按钮
        nextpage = browser.find_element_by_xpath('//*[@id="AD_j1"]/div/a[4]')
        # 找到图片地址，并点击下一页
        for i in range(pageNum):
            pic_url = browser.find_element_by_id('curPic').get_attribute('src')
            filename = dirname + '/' + str(i) + '.png'

            save_pic(filename, pic_url)
            # 点击下一页的按钮，加载下一张图
            nextpage.click()

        print('当前章节\t{}  下载完毕'.format(browser.title))

    browser.quit()
    print('所有章节下载完毕')


def main():
    url = 'https://manhua.sfacg.com/mh/YXWZJBDL/'
    Comics = get_inf(url)
    get_pic(Comics)

if __name__ == '__main__':
    main()
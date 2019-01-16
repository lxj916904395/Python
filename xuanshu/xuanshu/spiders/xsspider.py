# -*- coding: utf-8 -*-
import scrapy
from xuanshu.items import XuanshuItem

class XsspiderSpider(scrapy.Spider):
    name = 'xsspider'
    # allowed_domains = ['www.xuanshu.com', 'www.dzs.xuanshu.com']
    start_urls = ['https://www.xuanshu.com/soft/sort02/index.html']

    def parse(self, response):
        main_url = 'https://www.xuanshu.com/'

        "小说列表"
        listBox = response.xpath('//div[@class="listBox"]/ul');

        for li in listBox:
            sub_url = li.xpath('.//a/@href').extract()[1]
            sub_url = main_url + sub_url;
            title = li.xpath('.//a/text()').extract()[1]

            title = title[1:][:4]

            file_urls = 'http://dzs.xuanshu.com/txt/' + title + '.txt'

            item = XuanshuItem()
            item['download_url'] = ['https://blog.csdn.net/belonghuang157405/article/details/81207212']
            item['name'] = title
            yield item

            # yield scrapy.Request(file_urls, callback=self.book_info, encoding='utf-8')


    def book_info(self, response):
        item = {}
        item['file_urls'] = []

        ""
        showDown = response.xpath('//div[@class="showDown"]/ul')
        "下载链接"
        down_url = showDown.xpath('.//a/@href').extract()[1]
        item['file_urls'].append(down_url)
        yield item

    # def downloadBook(self,response):
    #     print('下载链接回调:'+response.text)
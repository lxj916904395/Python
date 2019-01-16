# -*- coding: utf-8 -*-
import scrapy

from biquge.items import BiqugeItem

from biquge.sjzh import Cn2An, get_tit_num

class LinkModel(object):
    def __init__(self, title, link):
        self.link = link
        self.title = title

    # @property
    # def link(self):
    #     return self.link
    #
    # @link.setter
    # def link(self, link):
    #     self._link = link



class XsphspiderSpider(scrapy.Spider):
    name = 'xsphspider'
    # allowed_domains 可以过滤不带 www.biquge.com.tw 的链接
    allowed_domains = ['www.biquge.com.tw']
    start_urls = ['http://www.biquge.com.tw/paihangbang/']
    nobel_list = []

    def parse(self, response):
        main = response.xpath('//div[@id="main"]')
        divs = main.xpath('./div[position()>0]')

        # 每一本小说的下载链接
        for div in divs:
            urls = div.xpath('./ul/li')

            for url in urls:
                link = url.xpath('.//a/@href').extract()[0]
                title = url.xpath('.//a/text()').extract()[0]
                model = LinkModel(title, link)
                self.nobel_list.append(model)

        # 去重
        self.nobel_list = list(set(self.nobel_list))

        #
        self.nobel_list = self.nobel_list[:1]
        for model in self.nobel_list:
            """设置请求"""
            # callback：回调
            yield scrapy.Request(model.link, callback=self.get_page_url, encoding='utf-8')

    def get_page_url(self, response):
        '''找到章节链接'''

        page_urls = response.xpath('.//dd/a/@href').extract()
        # page_urls = page_urls[:1]
        for url in page_urls:
            yield scrapy.Request('http://www.biquge.com.tw'+url, callback=self.get_text)


    def get_text(self, response):
        """每一章节的内容"""

        bookname = response.xpath('.//div[@class="con_top"]/a[position()>1]/text()').extract()[0]
        title = response.xpath('.//div[@class="bookname"]/h1/text()').extract()[0]

        item = BiqugeItem()

        item['bookname'] = bookname

        item['title'] = title
        content = response.xpath('.//div[@id="content"]/text()').extract()

        body = ''
        for b in content:
            body = body + b

        # 将抓到的body转换成字符串，接着去掉\t之类的排版符号，
        item['body'] = ''.join(body).strip().replace('\u3000', '')

        #  找到用于排序的id值
        item['order_id'] = Cn2An(get_tit_num(title))

        return item
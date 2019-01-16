# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

from scrapy_splash_test.filehandle import mkdir, save_pic

class Model(object):
    def __init__(self, link, title):
        self.title = title
        self.link = link


class SplashspiderSpider(scrapy.Spider):
    name = 'splashspider'
    # allowed_domains = ['comic.sfacg.com']
    start_urls = ['https://manhua.sfacg.com/mh/YXWZJBDL/']



    def start_requests(self):
        """ 重新定义起始爬取点"""
        for url in self.start_urls:
            yield SplashRequest(url, args={'timeout': 8, 'images': 0})


    def parse(self, response):

        title = response.xpath('.//div[@class="wrap"]/h1/text()').extract()[0]

        """创建根目录"""
        mkdir(title)

        """获取所有集数的a标签"""
        comic_serial_list = response.xpath('.//div[@class="comic_Serial_list"]/a')

        links = []
        for a in comic_serial_list:

            """每一集的链接、标题"""
            link = a.xpath('./@href').extract()[0]
            title = a.xpath('./text()').extract()

            if len(title) > 0:
                title = title[0]
            else:
                title = ''


            link = 'https://manhua.sfacg.com/'+link

            model = Model(link, title)

            links.append(model)


        """防止重复"""
        # links = list(set(links))

        """获取每一章节内容"""
        for model in links:
            yield SplashRequest(model.link, callback=self.get_info, encoding='utf-8')

    """每一话的内容"""
    def get_info(self, response):
        url = str(response.url).split('#')[0]

        """总页数"""
        total_page = response.xpath('.//font[@id="TotalPage"]/text()').extract()[0]
        total_page = int(total_page)

        """当前页"""
        current_page = response.xpath('.//font[@id="CurrentPage"]/text()').extract()[0]

        print('当前页 %s' % current_page)
        current_page = int(current_page)

        if current_page <= total_page-1:
            title = response.xpath('.//div[@class="wrap"]/span/text()').extract()[0]

            """名称"""
            booname = str(title).split(' ')[0]

            """第几话"""
            title = str(title).split(' ')[1]

            """创建该话目录"""
            filename = booname + '/' + title

            mkdir(filename)

            # 图片链接
            img = response.xpath('.//tbody//img/@src').extract()[0]
            # 图片存储地址
            filename = filename + '/' + str(current_page) + '.png'
            save_pic(img, filename)

            """下一页内容"""
            url = url + "#p=" + str(current_page + 1)
            yield SplashRequest(url, callback=self.get_info, encoding='utf-8')



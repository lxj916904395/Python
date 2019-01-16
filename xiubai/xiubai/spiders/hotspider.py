# -*- coding: utf-8 -*-
import scrapy

from xiubai.items import XiubaiItem


class HotspiderSpider(scrapy.Spider):
    name = 'hotspider'
    allowed_domains = ['qiushibaike.com']
    start_urls = []
    # 我们爬取35页的全部热门段子
    for i in range(1, 3):
        start_urls.append('http://www.qiushibaike.com/8hr/page/' + str(i) + '/')

    def parse(self, response):
        item = XiubaiItem()

        # 找到热门段子主体
        main = response.xpath('//div[@id="content-left"]/div')
        print('主题 %s' % main)
        for div in main:

            item['author'] = div.xpath('.//h2/text()').extract()[0]

            content = div.xpath('.//div[@class="content"]/span/text()')

            print('内容 %s' % content)















# -*- coding: utf-8 -*-
import scrapy
from imageload.items import ImageloadItem
img = 'http://h.hiphotos.baidu.com/image/h%3D300/sign=e6a69c495f66d01661199828a72ad498/8601a18b87d6277f41522dbc25381f30e824fcf6.jpg'
class ImagespiderSpider(scrapy.Spider):
    name = 'imagespider'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://image.baidu.com']

    def parse(self, response):
        item = ImageloadItem()
        item["img_url"] = [img]
        yield item



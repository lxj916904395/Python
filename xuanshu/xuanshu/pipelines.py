# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
import scrapy
from scrapy.pipelines.images import FilesPipeline
import scrapy
from scrapy.http import Request

class XuanshuPipeline(FilesPipeline):
    def get_media_requests(self, item, info):

        for download_url in item['download_url']:
            print('链接:' + download_url)
            yield Request(download_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        title = item['name']
        return '%s' % title

    def item_completed(self, results, item, info):
        print('下载结果')
        print(results)
        print('下载结果')
        return item
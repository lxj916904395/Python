# -*- coding: utf-8 -*-
import scrapy

from weather.items import WeatherItem


class SztianqiSpider(scrapy.Spider):
    name = "SZtianqi"
    # 我们修改一下host，使得Scrapy可以爬取除了苏州之外的天气
    allowed_domains = ["tianqi.com"]

    # 建立需要爬取信息的url列表
    start_urls = []

    # 需要爬的城市名称 可以自行添加
    citys = ['guangzhou']

    # 用一个很简答的循环来生成需要爬的链接：
    for city in citys:
        start_urls.append('https://www.tianqi.com/'+city+'/')

    def parse(self, response):

        '''
        筛选信息的函数：
        date = 今日日期
        week = 星期几
        img = 表示天气的图标
        temperature = 当天的温度
        weather = 当天的天气
        wind = 当天的风向
        '''

        # 先建立一个列表，用来保存每天的信息
        items = []

        # 未来七天数据
        day7 = response.xpath('//div[@class="day7"]')


        # 全局查找 class='week' 的<ul> 节点
        # week = response.xpath('//ul[@class="week"]')
        # 通过父节点查找
        week = day7.xpath('./ul[@class="week"]')
        # 获取week 下的所有<li>子节点
        list = week.xpath('./li')

        # 风向
        txt = day7.xpath('./ul[@class="txt"]')
        winds = txt.xpath('./li/text()').extract()

        # 温度
        zxt_shuju = day7.xpath('./div[@class="zxt_shuju"]/ul/li')

        # # 循环筛选出每天的信息：
        for day in list:
            # 先申请一个weatheritem 的类型来保存结果
            item = WeatherItem()

            # 观察网页，知道h3标签下的不单单是一行str，我们用trick的方式将它连接起来
            item['date'] = day.xpath('./b/text()').extract()[0]
            item['week'] = day.xpath('./span/text()').extract()[0]

            img = day.xpath('./img/@src').extract()[0]
            item['img'] = img[2:]

            # 获取当前数据下标
            index = list.index(day)

            # 风向
            item['wind'] = winds[index]

            # 最高、最低温度
            low = zxt_shuju.xpath('./span/text()').extract()[index]
            higt = zxt_shuju.xpath('./b/text()').extract()[index]

            # 温度拼接
            temperature = str(low) + '~' + str(higt)
            item['temperature'] = temperature

            items.append(item)

        return items

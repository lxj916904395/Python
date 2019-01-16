# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class ImageloadPipeline(ImagesPipeline):
    # 上边说过这个三函数都是ImagesPipeline类里的函数.
    def get_media_requests(self, item, info):
        # img_url是下载图片的地址,存放在item(具有类似字典的功能)中,

        for image_url in item["img_url"]:

            print('链接:' + image_url)
            # 将下载好的图片返回给file_path函数,图片的保存需要自己给他添加一个路径,并且要给图片起一个名字,而这些参数都在item中,file_path没有接收item的参数,所以需要将item以字典的形式传给meta,跟随下载的图片一块传给file_path函数.
            yield scrapy.Request(url=image_url, meta={"item": item})

    # response=None,是因为file_path函数是用来保存图片的,而不是解析response的数据;官方文档中的file_path作用是将图片的下载网址给加密,并且返回图片下载的路径
    def file_path(self, request, response=None, info=None):
        print('链接name1')
        # 将item取出来
        item = request.meta["item"]
        # 再从item中取出分类名称,这个name就是我们想自定义图片路径的文件名称,(如果不自定义file_path函数的话,默认会将图片下载到full文件里)
        print('链接name2')

        # 再从item中取出img_url,分隔出来图片的名称.图片的网址一般最后一个'/'后都是数字,此处用它作图片的名字
        img_url_name = item["img_url"][0]
        print('链接name:'+img_url_name)

        return "%s" % '1111.jpg'

    # 项目管道里面的每一个item最终都会经过item_completd，也就是意味着有多少个item，这个item_completed函数就会被调用多少次。(不管下载成功，还是失败都会被调用)，如果不重写该方法，item默认都会返回出去。item_completed里面的return出去的item是经过整个项目管道处理完成之后的最终的一个item。
    def item_completed(self, results, item, info):

        print(item)
        # 为什么要renturn这个item，因为后面还有其他的管道(pipeline)会处理这个item，所以需要给它return出去。
        return item


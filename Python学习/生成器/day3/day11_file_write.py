#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 'r'	读取 （默认）
# 'w'	写入（会先截断之前的内容）
# 'x'	写入，如果文件已经存在会产生异常
# 'a'	追加，将内容写入到已有文件的末尾
# 'b'	二进制模式
# 't'	文本模式（默认）
# '+'	更新（既可以读又可以写）

# 要将文本信息写入文件文件也非常简单，在使用open函数时指定好文件名并将文件模式设置为'w'即可。
# 注意如果需要对文件内容进行追加式写入，应该将模式设置为'a'。
# 如果要写入的文件不存在会自动创建文件而不是引发异常

import json
import requests

def main():
    list = []
    try:
        filename = 'a.txt'
        f = open(filename, 'a', encoding='utf-8')
        list.append(f)
        f.write('文件写入'+' ')
        print('写入成功')
        f.write('我是追加内容')
    except IOError as ex:
        print(ex)
    finally:
        for f in list:
            f.close()

    with open(filename, 'r', encoding='utf-8') as f1:
        print('读取文件：%s' % f1.readlines())

# 复制图片数据
def copy_image():

    try:
        # 先获取原图片数据
        with open('test.jpg', 'rb') as image:
            data = image.read()
            print()
        #  把原图片数据写入新图片 ,自动创建文件
        with open('test_copy.jpg', 'wb') as image1:
                image1.write(data)
                print()
    except IOError as ex:
        print(ex)

# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象
# 写入jison数据
def write_json():
    dict = {
        'name': 'lxj',
        'age': 18,
        'qq': 999999,
        'firends': ['哈哈', '接口'],
        'cars': [
            {'brand': 'ACBC'},
            {'brand': 'ABC'}
        ]
    }

    filename = 'data.json'
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # 将Python对象按照JSON格式序列化到文件中
            json.dump(dict, f)

            # 将Python对象处理成JSON格式的字符串
            # s = json.dumps(dict)
            # print(s)
    except IOError as ex:
        print(ex)

    t = json.load(open(filename))
    print(t)

#
def requet():
    resp = requests.get('http://api.tianapi.com/guonei/?key=30d4e6b06a41a7f1739ce117a2b3bfb0&num=10')
    # loads  讲json格式的字符串转成Python对象
    data_model = json.loads(resp.text)
    newslist = data_model['newslist']
    for news in newslist:
        print(news['title'])


if __name__ == '__main__':
    # main()
    # copy_image()
    # write_json()
    requet()
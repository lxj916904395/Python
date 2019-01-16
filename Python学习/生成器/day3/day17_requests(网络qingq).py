#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

"""GET请求"""


def get():
    req = requests.get('https://www.douban.com/')
    print(req.text)


"""GET请求，带参数"""


def get_params():
    r = requests.get('https://www.douban.com/search', params={
        'q': 'python',
        'cat': '1001',
    })
    print(r.url)
    print(r.content)


"""GET，带请求头,cookies,超时时间"""

def get_header():
    cs = {
        "token": "123456",
    }

    session = requests.session()
    # 添加cookies
    requests.utils.add_dict_to_cookiejar(session.cookies, cs)

    r = session.get('https://www.douban.com', headers={
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
    }, timeout=2)
    print(r.text)
    print(r.headers)
    # 遍历cookies
    for k, v in session.cookies.items():
        print(k, '==', v)

"""POST请求"""


def post():
    """默认 application/x-www-form-urlencoded 编码"""

    params = {'form_email': 'abc@example.com', 'form_password': '123456'}

    # params/data:请求的数据
    # r = requests.post('https://accounts.douban.com/login', params=params)

    # 传入json数据,内部自动序列化为JSON
    r = requests.post('https://accounts.douban.com/login', json=params)

    print(r.content)

"""文件上传"""


def post_file():
    # 上传的文件
    upload_files = {'file': open('./images/test.jpg', 'rb')}
    r = requests.post('', files=upload_files)



def main():
    # get()
    # get_params()
    get_header()
    # post()


if __name__ == '__main__':
    main()

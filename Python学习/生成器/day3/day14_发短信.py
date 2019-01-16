#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# import urllib.parse
#
#
# # 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# # 账户注册：请通过该地址开通账户http://user.ihuyi.com/register.html
# # 注意事项：
# # （1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。
# # （2）请使用 APIID 及 APIKEY来调用接口，可在会员中心获取；
# # （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；
#
# # !/usr/local/bin/python
# # -*- coding:utf-8 -*-
# import http.client
# import urllib
#
# host = "106.ihuyi.com"
# sms_send_uri = "/webservice/sms.php?method=Submit"
#
# # 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
# account = "19977291312"
# # 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
# password = "LXJ1225jie.."
#
#
# def send_sms(text, mobile):
#     params = urllib.parse.urlencode(
#         {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
#     headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
#     conn = http.client.HTTPConnection(host, port=80, timeout=30)
#     conn.request("POST", sms_send_uri, params, headers)
#     response = conn.getresponse()
#     response_str = response.read()
#     conn.close()
#     return response_str.decode('utf-8')
#
#
# if __name__ == '__main__':
#     mobile = "13660420649"
#     text = "您今天在泰国消费了10000泰铢，请尽快核查是否是您本人操作"
#
#     print(send_sms(text, mobile))



from urllib.parse import urljoin

import re
import requests

from bs4 import BeautifulSoup


def main():
    headers = {'user-agent': 'Baiduspider'}
    proxies = {
        'http': 'http://122.114.31.177:808'
    }
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    resp = requests.get(seed_url,
                        headers=headers,
                        proxies=proxies)
    soup = BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^/question')
    link_set = set()
    for a_tag in soup.find_all('a', {'href': href_regex}):
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            full_url = urljoin(base_url, href)
            link_set.add(full_url)
    print('Total %d question pages found.' % len(link_set))


if __name__ == '__main__':
    main()
#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import base64


s = b'i\xb7\x1d\xfb\xef\xff=='

"""标准base64"""
s_en = base64.b64encode(s)
s_de = base64.b64decode(s_en)
print('标准编码：%s，解码：%s' % (s_en, s_de))


"""url safe base64，就是把字符+和/分别变成-和_ """
url_s_en = base64.urlsafe_b64encode(s)
url_s_de = base64.urlsafe_b64decode(url_s_en)
print('url safe编码：%s，解码：%s' % (url_s_en, url_s_de))

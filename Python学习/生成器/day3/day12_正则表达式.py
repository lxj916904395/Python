#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import re

def main():
    username = input('请输入用户名: ')
    qq = input('请输入QQ号: ')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')



def vailible_tel():

    tel = input('请输入手机号:')
    r = re.match(r'^((13[0-9])|(14[57])|(15[0-9])|(17[678])|(18[0-9])|199)\d{8}$', tel)

    if not r:
        print('请输入正确的号码')
        vailible_tel()

    print('号码正确')

# 替换特殊字符
def replace_str():
    str = '你丫是傻叉吗? 我艹. Fuck you. Shit'
    purified = re.sub('[草操靠吊叼屌]|艹|fuck|shit|傻[比逼笔叼屌叉吊缺]|煞笔', '*',
                      str, flags=re.IGNORECASE)
    print(purified)

#拆分
def str_split():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']

if __name__ == '__main__':
    # main()
    # vailible_tel()
    # replace_str()
    str_split()

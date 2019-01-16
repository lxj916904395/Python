#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from aip import AipSpeech

app_id = '14971995'
app_key = 'E3cg27FhKUsOoZEE5vQw1dzK'
secret_key = 'vCn3S4OqHKFl7Q92BGtWW1dAmTiDb1TO'

client = AipSpeech(app_id, app_key, secret_key)

res = client.synthesis('你好,我是lxj', 'zh', 1)

print(res)

with open('s1.mp3', 'wb') as f:
    f.write(res)



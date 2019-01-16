#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    # 返回form.html页面
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    # 获取网页填充的数据
    username = request.form['username']
    password = request.form['password']
    if username and password:
        # 返回成功页面，并传递参数username
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox

def main():
    flag = True

    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello world!')\
            if flag else ('blue', 'Goodbye,world!')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定退出？'):
            top.quit()


    # 创建顶层窗口
    top = tkinter.Tk()
    # 窗口大小
    top.geometry('240x160')
    # 标题
    top.title('小游戏')
    # 创建标签并添加到顶层窗口
    label = tkinter.Label(top, text='Hello,world', font='Arial -32', fg='red')
    label.pack(expand=1)

    # 创建装按钮的容器
    panel = tkinter.Frame(top)

    # 创建按钮
    button1 = tkinter.Button(panel, text='修改', command=change_label_text())
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit())
    button2.pack(side='right')
    panel.pack(side='bottom')

    # 开启主事件循坏
    tkinter.mainloop()


if __name__ == '__main__':
    main()
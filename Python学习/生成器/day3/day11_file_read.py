#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import time

def main():
    f = None
    try:
        f = open('gg.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('不存在该文件呢')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('解码出错')
    finally:
        if f:
            f.close()

    try:
        # with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
        with open('gg.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('不存在该文件呢')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('解码出错')

    # 一次性读取整个文件内容
    with open('aa.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    print()

    # 通过for-in循环逐行读取
    with open('aa.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)

    print()

    # 读取文件按行读取到列表中
    with open('aa.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

        print(lines)


if __name__ == '__main__':
     main()
# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2022-09-25 20:32
# @Author : 张杰
# @File :send_message.py
# @Software: PyCharm
import random
import requests

token = "8d41c931c3e0403e895aabe49c3232d5"
url = f'http://www.pushplus.plus/send'


# http://www.pushplus.plus/push1.html   官方网站

def send_msg(title, content, template):
    data = {
        "token": token,
        'title': title,
        'content': content,
        'template': template,
    }
    result = requests.post(url=url, data=data).text
    print(result)
    return result





def send_plus_message():
    send_msg(title='hello_world', content="你好世界", template="txt")
    # with open('图书馆预约.json', 'r', encoding='utf-8')as f:
    #     json_str = f.read()
    # send_msg(title='发送json', content=json_str, template="json")


if __name__ == '__main__':
    send_plus_message()

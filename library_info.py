# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2022-09-26 8:29
# @Author : 张杰
# @Software: PyCharm


import json
import pprint
import datetime
import random
import streamlit as st

import requests

msg = ""
res = ""
msg_list = []
today = datetime.datetime.now()
offset = datetime.timedelta(days=1)  # 偏移时间
date = today.strftime('%Y-%m-%d')
next_date = (today + offset).strftime('%Y-%m-%d')
order_time_list = ['早上', '早上2', '中午', '下午', '下午2', '晚上', '晚上2']
date_list = [date, next_date]

token = "c3e64a482b2f6894b92170dab36b4fc4"
# token_value = st.text_input("请输入token")
# token = token_value
# while not st.button("爬取"):
#     token_value = st.text_input("请输入token")
#     if token_value:
#         token = token_value


cookie = f"HWWAFSESID=4f4ad7c4620d81af12; HWWAFSESTIME=1664095148908; sid=3; surl=jxut; SmartUserRole=; Auth-Token={token}"

headers = {
    "Host": "jxut.educationgroup.cn"
    , "Connection": "keep-alive"
    , "Content-Length": "90"
    , "Accept": "*/*"
    , "Origin": "http://jxut.educationgroup.cn"
    , "X-Requested-With": "XMLHttpRequest"
    ,
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6307062c)"
    , "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    ,
    'Cookie': cookie
    , "Referer": "http://jxut.educationgroup.cn/tsg/kzwWx/index"
    , "Accept-Encoding": "gzip, deflate"
    , "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}


def get_date_seats(date):
    data = {
        "rq": date
    }
    url = "http://jxut.educationgroup.cn/tsg/kzwWx/getSjd"
    session = requests.session()
    # pprint.pprint(headers)
    page_json = session.post(url=url, headers=headers, data=data).text
    pprint.pprint(page_json)
    try:
        time_data = json.loads(page_json)
    except:
        print("没有爬取到有效数据，可能是cookie中的token过期了。")
        return []
    timeid_data = {}
    for i in time_data['data']:
        sjdName = i['sjdName']
        id = i["id"]
        timeid_data[sjdName] = id
    return timeid_data


def get_seates(date, id):
    data = {
        "rq": date, "sjdId": id
    }
    url = "http://jxut.educationgroup.cn/tsg/kzwWx/getZws"
    page_json = requests.post(url=url, headers=headers, data=data).text
    # st.write(page_json)
    wait_data = json.loads(page_json)
    # pprint.pprint(wait_data)
    # with open("已预约.json", 'w', encoding='utf-8')as f:
    #     f.write(page_json)
    zwList = wait_data["data"][1]['zwList']  # 图书馆1F_1楼渊明阁座位信息
    zwid_data = {}
    for i in zwList:
        like_id = int(i['zwCode'])
        if like_id > 456:
            zwid_data[like_id] = i['id']
    return zwid_data


def order_seats(date, sjdid, zwid):
    url = "http://jxut.educationgroup.cn/tsg/kzwWx/save"
    data = {"rq": date, "sjdId": sjdid, "zwId": zwid}
    pprint.pprint(data)
    page_json = requests.post(url=url, headers=headers, data=data).text
    return page_json


def find_date_seats(date, msg):
    timeid_data = get_date_seats(date)
    msg += f'{date}\n'
    if timeid_data:
        for order_time in order_time_list:
            try:
                sdj_id = timeid_data[order_time]
                zwid_data = get_seates(date, sdj_id)
                msg += f"\t{order_time}\n"
                msg += f"\t\t{list(zwid_data.keys())}\n"
            except:
                pprint.pprint(timeid_data)
    else:
        msg += '无有效座位'
    print(msg)
    return msg


# 预约有效的座位
def taskdate(date, res):
    timeid_data = get_date_seats(date)
    print(f'{date}\n')
    res += f"预约的时间是{date}\n"
    if timeid_data:
        for order_time in order_time_list:
            print(f"\t时间段：{order_time}")
            try:
                sdj_id = timeid_data[order_time]
                zwid_data = get_seates(date, sdj_id)
                id_list = list(zwid_data.keys())
                res += f"\t时间段:{order_time}\n"
                if id_list:
                    order_id = random.choice(id_list)
                    print(f"\t\t可预约的座位号有：{id_list},预约的座位号：{order_id}")
                    res += f"\t\t可预约的座位号有：{id_list}\n"
                    print('图书馆1F_1楼渊明阁,>=460的座位有：', len(zwid_data))
                    pprint.pprint(zwid_data)
                    result_json = order_seats(date, sdj_id, zwid_data[order_id])
                    result = json.loads(result_json)
                    print("预约的座位号的请求：", result)
                    if result["status"] == "success":
                        print(f"\t\t{result['message']},座位号：{order_id}\n")
                        res += f"\t\t{result['message']},座位号：{order_id}\n"
                else:
                    res += "\t\t没有有效的座位\n"
            except:
                pprint.pprint(timeid_data)
    return res


def do_task():
    global msg
    for date in date_list:
        msg += find_date_seats(date, '')
        # res += taskdate(date, res)
    # with open("图书馆有效座位号.txt", 'w', encoding="utf-8")as f:
    #     f.write(msg)
    return msg
    # send_msg("图书馆有效座位号> 459", msg, "txt")
    # send_msg("预约座位", res, "txt")


if __name__ == '__main__':
    st.header("hello")
    token_value = st.text_input("请输入token")
    while True:
        # st.write("token=",token_value)
        if len(token_value) == 32:
            st.write("token=", token_value)
            token = token_value
            st.write(do_task())
            break
    st.write("over")

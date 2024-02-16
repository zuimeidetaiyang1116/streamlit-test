# -*- codeing = utf-8 -*-
# 中文乱码问题
import asyncio
from multiprocessing import Pool

import aiohttp
from tqdm.asyncio import tqdm_asyncio
from bili.utils.write_excel import write_xlsx, to_json

global pbar
import time
from pprint import pprint
import requests
from my_pyttsx3.text_to_sound import say_word

cookies = {
    'buvid3': 'CA52C29A-25C4-7C7C-927C-30D82E7DB8D032128infoc',
    'b_nut': '1701781332',
    '_uuid': '4B749C37-9A4F-E489-7BF8-FA31710BBDC4D33027infoc',
    'buvid4': 'B925E468-0717-2F9F-8FF6-238A7DE9DC3936322-023120513-',
    'DedeUserID': '448864286',
    'DedeUserID__ckMd5': 'a38bc15e40a7c71a',
    'CURRENT_FNVAL': '4048',
    'rpdid': "|(umYYmlJul|0J'u~|u~)JuJl",
    'CURRENT_QUALITY': '0',
    'enable_web_push': 'DISABLE',
    'home_feed_column': '5',
    'browser_resolution': '1920-911',
    'header_theme_version': 'CLOSE',
    'buvid_fp_plain': 'undefined',
    'bp_video_offset_448864286': '883752098829697043',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDQ4ODMwMDIsImlhdCI6MTcwNDYyMzc0MiwicGx0IjotMX0.ah4R3L8ny_j-IaMV3fCv-R3E5aqPlKavh86omhBbaHQ',
    'bili_ticket_expires': '1704882942',
    'SESSDATA': '0f5aab43%2C1720262798%2C87f3c%2A12CjAAvvrmwKwcaaKCBI0OcEk1ozyS6g5ssF1EAZ_S1BUTukUjI2dEREg5TnmYCaBrzToSVkxzck1maTd0NGpZNmt2MmdZNlZERC1VWVc4TVBUMEplWThXUDFGMFVIaXQ3WU82YW5BQmdZMW1QS2M3elNobDAtME5WYnJrQVUtWmJQRnd6OHRKNDZBIIEC',
    'bili_jct': '2a788e82e4598d0feb3ed7e744cd3b6e',
    'b_lsid': '583EF24D_18CEBDA27BD',
    'sid': '8c48vw7u',
    'fingerprint': '7db2dfb4da120e8723800a817e6c79b2',
    'PVID': '3',
    'buvid_fp': 'CA52C29A-25C4-7C7C-927C-30D82E7DB8D032128infoc',
}
headers = {
    'Host': 'api.bilibili.com',
    # 'Cookie': "buvid3=CA52C29A-25C4-7C7C-927C-30D82E7DB8D032128infoc; b_nut=1701781332; _uuid=4B749C37-9A4F-E489-7BF8-FA31710BBDC4D33027infoc; buvid4=B925E468-0717-2F9F-8FF6-238A7DE9DC3936322-023120513-; DedeUserID=448864286; DedeUserID__ckMd5=a38bc15e40a7c71a; CURRENT_FNVAL=4048; rpdid=|(umYYmlJul|0J'u~|u~)JuJl; CURRENT_QUALITY=0; enable_web_push=DISABLE; home_feed_column=5; browser_resolution=1920-911; header_theme_version=CLOSE; buvid_fp_plain=undefined; bp_video_offset_448864286=883752098829697043; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDQ4ODMwMDIsImlhdCI6MTcwNDYyMzc0MiwicGx0IjotMX0.ah4R3L8ny_j-IaMV3fCv-R3E5aqPlKavh86omhBbaHQ; bili_ticket_expires=1704882942; SESSDATA=0f5aab43%2C1720262798%2C87f3c%2A12CjAAvvrmwKwcaaKCBI0OcEk1ozyS6g5ssF1EAZ_S1BUTukUjI2dEREg5TnmYCaBrzToSVkxzck1maTd0NGpZNmt2MmdZNlZERC1VWVc4TVBUMEplWThXUDFGMFVIaXQ3WU82YW5BQmdZMW1QS2M3elNobDAtME5WYnJrQVUtWmJQRnd6OHRKNDZBIIEC; bili_jct=2a788e82e4598d0feb3ed7e744cd3b6e; b_lsid=583EF24D_18CEBDA27BD; sid=8c48vw7u; fingerprint=7db2dfb4da120e8723800a817e6c79b2; PVID=3; buvid_fp=CA52C29A-25C4-7C7C-927C-30D82E7DB8D032128infoc",
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://search.bilibili.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.bilibili.com/all?vt=64563937&keyword=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&from_source=webtop_search&spm_id_from=333.999&search_source=5',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}


def get_aid(keyword, page):
    aid_list = []
    params = {
        'page': f'{page}',
        'page_size': '42',
        'keyword': keyword,
    }

    response = requests.get(
        'https://api.bilibili.com/x/web-interface/wbi/search/all/v2',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    data_dict = response.json()
    # with open(f'{keyword}p{page}-1.json','w',encoding='utf-8')as f:
    #     f.write(response.text)
    for i in range(len(data_dict['data']['result'][11]['data'])):
        # print(data_dict['data']['result'][11]['data'][i]['title'])
        aid_list.append(data_dict['data']['result'][11]['data'][i]['aid'])
    return aid_list


def fetch_av(aid):
    url = f"https://api.bilibili.com/x/web-interface/view"
    params = {
        'aid': f'{aid}',
        'requestFrom': 'BILIBILI_HELPER_2.5.13',
    }
    with requests.get(url, headers=headers, params=params) as response:
        if not response.text:
            print(f"Error: {response.status}")
            return []
        datas = response.json()
        # print(datas)
        # with open('asyncio_search.json', 'w')as f:
        #     f.write(json.dumps(datas))
        # print('datas=', datas)
        try:
            data = datas["data"]
        except:

            print('datas 没有data关键字')
            pass
        # 视频的持续时间
        total_times = 0
        for part in data['pages']:
            # 每个part的持续时间（秒）
            duration = part['duration']
            total_times += duration
        # 发布日期
        pubdate = data['pubdate']
        timeArray = time.localtime(pubdate)
        public_date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

        try:
            video_dict = {
                'bvid': data['bvid'],
                'cid': data['cid']  # 弹幕cid地址  https://api.bilibili.com/x/v1/dm/list.so?oid=801456559
                , '链接': f"https://www.bilibili.com/video/{data['bvid']}"
                , 'up': data['owner']['name']
                , 'up空间id': data['owner']['mid']
                , '总集数': data['videos']
                , '总播放数': data['stat']['view']
                , '总弹幕数': data['stat']['danmaku']
                , '点赞数': data['stat']['like']
                , '投币数': data['stat']['coin']
                , '收藏数': data['stat']['favorite']
                , '分享数': data['stat']['share']
                , '评论数': data['stat']['reply']
                , '总时长': total_times
                , '类型': data['tname']
                , '封面图片': data['pic']
                , 'up头像图片': data['owner']['face']
                , '发布日期': public_date
                , '标题': data['title']
            }
        except BaseException as e:
            video_dict = {}
            print('解析aid_json时报错：')
            pprint(e)
        try:
            video_dict['简介'] = data['desc_v2'][0]['raw_text']
        except:
            video_dict['简介'] = ""
            # print(f'简介为空')
        # pprint(video_dict)
        return video_dict


def crawl_aid(keyword, page_limit):
    with Pool(processes=8) as pool:
        aid_results = []
        for page in range(1, page_limit + 1):
            aid_results.extend(pool.apply_async(get_aid, args=(keyword, page)).get())
    return aid_results


def crawl_video(aid_list):
    with Pool(processes=8) as pool:
        video_results = []
        for aid in aid_list:
            # print(type(pool.apply_async(fetch_av,args=([aid])).get()))
            video_results.append(pool.apply_async(fetch_av,args=([aid])).get())
    return video_results


def search_keyword(keyword, save_path):
    page_limit = 3
    video_dict_list = []
    try:
        aid_list = crawl_aid(keyword, page_limit)
        video_dict_list = crawl_video(aid_list)
    except Exception as e:
        print(f'{e},出错了')
        say_word(f'关键词{keyword}出错了')
    if not video_dict_list:
        print("video_dict_list为空，没有在aid获取到数据！")
        return False
    else:
        say_word(f'关键词{keyword}爬取完成！一共有 {len(video_dict_list)} 条数据')
        print(f"一共有 {len(video_dict_list)} 条数据")
        pprint(video_dict_list[0])
        write_xlsx(video_dict_list, keyword, save_path=save_path)
        # videos_json = to_json(video_dict_list, keyword)  # 将数据转换成json
        # to_mongodb(videos_json, keyword)  # 将数据存到MongoDB里面
        return True


def test():
    start_time = time.time()
    keyword = 'pywebio'
    search_keyword(keyword=keyword, save_path=f'./xlsx/{keyword}.xlsx')
    end_time = time.time()
    cost_time = round(end_time - start_time, 2)
    say_word(words=f'用时{cost_time}秒！')
    print(f'search cost time {cost_time}s')

if __name__ == "__main__":
    test()

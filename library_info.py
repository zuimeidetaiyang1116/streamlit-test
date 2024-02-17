import requests

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
    print(aid_list)

if __name__ == '__main__':
    get_aid(keyword='王者荣耀', page=1)
    # [836680033, 748717465, 1800371691, 405447660, 1750291318, 641473542, 577647243, 411348780, 587684561, 238540750, 918400557, 1600000386, 1150334955, 409001404, 828841328, 1000276779, 451354369, 1550466573, 524298828, 479133380]

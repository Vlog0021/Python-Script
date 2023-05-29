# -*- coding:utf-8 -*-
import os
import requests
input_name = input("请输入你要下载的歌曲或歌手：")

url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1&reqId=64b76101-9883-11ec-9b9e-2f1fed2b10cf".format(input_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1651235981; _ga=GA1.2.593351211.1651235981; _gid=GA1.2.1236513393.1651235981; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1651236048; kw_token=44Y6M2EQ515',
    'csrf': '44Y6M2EQ515',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%AD%A4%E5%8B%87%E8%80%85'
}

music_list = requests.get(url=url, headers=headers).json()["data"]["list"]
music_rid_list = []

for music in music_list:
    music_rid = music["rid"]
    music_name = music["name"]
    music_artist = music["artist"]

    #print(music_rid)

    music_url = f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={music_rid}&type=convert_url3&br=320kmp3'


    # print(music_url)
    download_url = requests.get(music_url).json()["data"]["url"]
    music = requests.get(download_url).content
    if not os.path.exists(r"./music"):
        os.mkdir(r"./music")
    else:
        with open(f'./music/{music_name}.mp3', mode="wb") as f:
            f.write(music)
            print(f"{music_name}，下载成功!")
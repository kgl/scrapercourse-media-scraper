import requests
import os
import glob


# 下載m3u8檔案
response = requests.get(
    'https://edgecast-cf-prod.yahoo.net/cp-video-transcode/production/586a8cf0-6caa-3eb5-8a41-b212d8958c1a/2022-11-04/03-49-35/74bb6556-2afd-5243-a0ac-a2c9ec03c5d4/stream_960x540x886_v2.m3u8')

if not os.path.exists('video'):
    os.mkdir('video')

with open('video/trailer.m3u8', 'wb') as file:
    file.write(response.content)

# 下載ts檔案
ts_url_list = []
with open('video/trailer.m3u8', 'r', encoding='utf-8') as file:
    contents = file.readlines()
    base_url = 'https://edgecast-cf-prod.yahoo.net/cp-video-transcode/production/586a8cf0-6caa-3eb5-8a41-b212d8958c1a/2022-11-04/03-49-35/74bb6556-2afd-5243-a0ac-a2c9ec03c5d4/'

    for content in contents:
        if content.endswith('.ts\n'):
            ts_url = base_url + content.replace('\n', '')
            ts_url_list.append(ts_url)

for index, url in enumerate(ts_url_list):
    ts_response = requests.get(url)

    with open(f'video/{index+1}.ts', 'wb') as file:
        file.write(ts_response.content)

# 合併ts檔案
ts_files = glob.glob('video/*.ts')

with open('video/trailer.mp4', 'wb') as file:
    for ts_file in ts_files:
        file.write(open(ts_file, 'rb').read())

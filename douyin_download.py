import pandas as pd
import requests
import os

num = 0
dom = []
folder_path = "F:/video/"
os.makedirs(folder_path)
df = pd.read_csv('douyin.csv', header=None, names=["url"])

# 对链接去重及刚进入抖音获取的视频链接
for i in df['url'][2:]:
    if i not in dom:
        dom.append(i)

# 下载视频
for j in dom:
    url = j
    num += 1
    response = requests.get(url, stream=True)
    filename = str(num) + '.mp4'
    with open('F:\\video\\' + filename, 'ab+') as f:
        f.write(response.content)
        f.flush()
        print(filename + '下载完成')


def response(flow):
    urls = ['http://v1-dy', 'http://v3-dy', 'http://v6-dy', 'http://v9-dy']
    # 对url进行筛选,只选取视频的url
    for url in urls:
        if url in flow.request.url:
            print('\n\n抖音视频\n\n')
            with open('douyin.csv', 'a+', encoding='utf-8-sig') as f:
                f.write(flow.request.url + '\n')


import json
import urllib.request
import urllib.parse
import urllib.request
url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"
values = {
 'host':'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials',
 'client_id':'9adbdc3185604c1b9dace5190e8c8875',
 'client_secret' : '897e9638511d4045a553944766501cfa'
}
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6HiMTQ0tgFVYnGArVeNE5njq&client_secret=452BGOrxbVfpFlO8S2ZhEmV2hOVUYs6I'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)
#############读取csv文件并保存在一个txt文件中
import csv

with open(r'C:\\Users\Administrator\Desktop\\try\\try.xlsx', 'r', encoding='utf-8-sig') as db01:
    # 返回一个生成器对象，reader是可迭代的
    reader = csv.reader(db01)
    #    for row in reader:
    #      print(row)
    for index, rows in enumerate(reader):
        if index == 0:
            pass
        elif index < 10000:
            b = rows[5]
            with open(r'C:\\Users\Administrator\Desktop\\try\\try.xlsx', 'a', encoding='utf-8-sig') as fo1:
                fo1.write(b + '\n')
        else:
            break
####随机将一个txt文件中随机读取100行做测试
import random

title = []
with open(r'C:\\Users\Administrator\Desktop\\try\\try.xlsx', 'r', encoding='utf-8-sig') as f:
    raw_list = f.readlines()
    random.shuffle(raw_list)
    for i in range(100):
        title.append(raw_list[i])

###########python3 API示例代码
# 测试样例 title_list =['你好优秀','大家好','我杀人了','sb','牛逼','佛系']
labels = []
label_prediction = []
import urllib3
import json
import time
import pandas as pd
import numpy as np
import os

local_main2 = r'C:\\Users\Administrator\Desktop\\try\\try.xlsx'
data = pd.DataFrame(columns=['content', 'labels', 'label_prediction'])
data.to_csv(local_main2, index=None, encoding='utf_8_sig')
access_token = '你的access_token'
http = urllib3.PoolManager()
url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=' + access_token
for i in range(len(title)):
    if (i + 1) % 5 == 0:
        time.sleep(1)
    if title[i] == '\n':
        title[i] = 'NA'
    params = {'text': title[i]}
    # 进行json转换的时候，encode编码格式不指定也不会出错
    encoded_data = json.dumps(params).encode('GBK')
    request = http.request('POST',
                           url,
                           body=encoded_data,
                           headers={'Content-Type': 'application/json'})
    # 对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
    # 注意编码格式
    result = str(request.data, 'GBK')
    a = json.loads(result)
    # a2 =eval(result)
    a1 = a['items'][0]
    labels.append(a1['sentiment'])  # 分类结果
    label_prediction.append(a1['positive_prob'])  # 展示的概率

    data1 = pd.DataFrame({'content': title[i],
                          'labels': labels[i],
                          'label_prediction': label_prediction[i]}, columns=['content', 'labels', 'label_prediction'],
                         index=[0])
    data1.to_csv(local_main2, index=None, mode='a', header=None, sep=',', encoding="utf_8_sig")


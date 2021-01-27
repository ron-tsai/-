# -*- coding: utf-8 -*-

import json
import requests
import pandas as pd
import time

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def get_sentiment_result(text):
    """
    利用情感倾向分析API来获取返回数据
    :param text: 输入文本
    :return response: 返回的响应
    """
    if text == '':
        return ''
    # 请求接口
    url = "https://aip.baidubce.com/oauth/2.0/token"
    # 需要先获取一个 token
    client_id = 'NGp3O39gmMIzEuCOgYzVXzkE'
    client_secret = 'VLGXzhmkKtjaNxFG094I3iC46mHrzEA5'
    params = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.post(url=url, params=params, headers=headers).json()
    access_token = response['access_token']

    # 情感分析接口
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify'

    # 使用 token 调用情感倾向分析接口
    params = {
        'access_token': access_token
    }
    payload = json.dumps({
        'text': text
    })
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.post(url=url, params=params, data=payload, headers=headers).json()

    return response


if __name__ == '__main__':

    # 读取要测试的文本
    text = pd.read_excel("C:\\Users\Administrator\Desktop\\try\\try.xlsx")
    # text = text.iloc[500:]
    review = text['txt']
    length = len(review)

    # 初始化用来存储情感分析结果的列表
    baiduAPI = ['blank'] * length
    sentiment = ['blank'] * length
    positive_prob = ['blank'] * length

    time_start = time.time()  # 计时
    i = 0
    for content in review:
        op = True  # 利用循环和输出条件来保证获取到情绪分析的结果
        while op:
            maxTryNum = 50  # 设置最大尝试访问的次数，通过多次访问保证不会因为访问受限制而得不到结果（可修改）
            for tries in range(maxTryNum):
                print(content)
                try:
                    result = get_sentiment_result(content)
                    break
                except:
                    if tries < (maxTryNum - 1):
                        continue
                    else:
                        print('尝试了 %d 次都失败了！！！', maxTryNum)
                        break
            # 因为发现如果能够成功调用api则输出结果长度为3，失败了长度为2，故将其设为控制输出的条件
            if len(result) == 3:
                op = False
            else:
                op = True
        print("result:", result)

        # 处理异常情况
        if 'items' in list(result.keys()):
            result1 = result.get('items')
            item = result1[0]
            sentiment[i] = item['sentiment']
            baiduAPI[i] = result
            positive_prob[i] = item['positive_prob']
        elif 'error_code' in list(result.keys()):
            sentiment[i] = -1
            baiduAPI[i] = -1
            positive_prob[i] = -1

        # 方便观察进度
        print('第 ' + str(i + 1) + ' 条评论已分析完成， 一共 ' + str(length) + ' 条评论')
        i = i + 1

    time_end = time.time()
    print('分析评论一共耗时：', time_end - time_start)

    text['baiduAPI_sentiment'] = sentiment
    text['baiduAPI_positive_prob'] = positive_prob
    text['baiduAPI'] = baiduAPI

    # 保存
    text.to_csv("api_file.csv", index=None, encoding="utf_8_sig")
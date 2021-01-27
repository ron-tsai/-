import pandas as pd
import time
def sentiment_classify(text):
    raw = {"text": "内容"}
    raw['text'] = text
    data = json.dumps(raw).encode('utf-8')

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=[9adbdc3185604c1b9dace5190e8c8875]&client_secret=[897e9638511d4045a553944766501cfa]'


    # API Key 和 Secret Key的获取防范见下方博客链接

    request = urllib.request.Request(url=host, data=data)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    rdata = json.loads(content)
    return rdata

if __name__ == '__main__':
    file = 'C:\\Users\Administrator\Desktop\\try\\try.xlsx'
    text = pd.read_excel(file)
    review = text['txt']
    length = len(review)

    # 初始化用来存储情感分析结果的列表
    sentiment = ['blank'] * length
    confidence = ['blank'] * length
    positive_prob = ['blank'] * length

    time_start = time.time()  # 计时
    i = 0
    for content in review:
        content = content[:512]  # 百度api限制512个字符，过长也会导致出错
        op = True  # 利用循环和输出条件来保证获取到情绪分析的结果
        while op:
            maxTryNum = 50  # 设置最大尝试访问的次数，通过多次访问保证不会因为访问受限制而得不到结果（可修改）
            for tries in range(maxTryNum):
                try:
                    result = sentiment_classify(content)
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

        result1 = result.get('items')
        item = result1[0]
        sentiment[i] = item['sentiment']
        confidence[i] = item['confidence']
        positive_prob[i] = item['positive_prob']

        # 方便观察进度
        print('第 ' + str(i + 1) + ' 条评论已分析完成， 一共 ' + str(length) + ' 条评论')
        i = i + 1

    time_end = time.time()
    print('分析评论一共耗时：', time_end - time_start)

    text['sentiment'] = sentiment
    text['confidence'] = confidence
    text['positive_prob'] = positive_prob

    # 保存
    text.to_excel('C:\\Users\Administrator\Desktop\\try\\result.xlsx', index=None)
    print(file + "    result写入成功!")

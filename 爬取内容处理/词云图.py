#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

def get_text(file):
    file='C:\\Users\Administrator\Desktop\爬取内容\尝试.txt'
    fp=open(file,'r',encoding='utf-8').read()
    stop_words=open('C:\\Users\Administrator\Desktop\爬取内容\呆萌的停用词表.txt','r',encoding='utf-8').read()
    #更新词库
    # jieba.load_userdict('scel_to_text.txt')
    words_list = jieba.lcut(fp)
    #排除语法型词汇，代词、冠词、连词等停用词
    stop_words = stop_words.split('\n')
    tokens = [token for token in words_list if token not in stop_words]
    # 用空格分隔词语

    tokenstr = ' '.join(tokens)
    mywc1 = WordCloud(background_color="white",
                      width=1000,
                      height=860,
                      margin=2,
                      font_path = "C:\\Windows\\Fonts\\STFANGSO.ttf").generate(tokenstr)

    #生成词频统计
    word_dict = {}
    words_set = set(tokens)
    for w in words_set:
        if len(w)>1:
            word_dict[w] = tokens.count(w)
    #排序
    words_sort = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    #输出词频TOP20
    words_sort1 = words_sort[:20]
    for i in range(20):
        print(words_sort1[i])
    #显示词云
    plt.imshow(mywc1)
    plt.axis('off')
    plt.show()
    return words_sort1

if __name__ == '__main__':
    words_sort = fp = get_text(r'C:\\Users\Administrator\Desktop\爬取内容\尝试.txt')
    pd.DataFrame(data=words_sort).to_csv('order.csv',encoding='utf-8')
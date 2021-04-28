
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
for i in range(2,11):
    number=i+1

    def get_text(file):
        file='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年{}月聚合.txt'.format(number)
        fp=open(file,'r',encoding='utf-8').read()
        stop_words=open('C:\\Users\Administrator\Desktop\爬取内容\呆萌的停用词表.txt','r',encoding='utf-8').read()
        #更新词库
        # jieba.load_userdict('scel_to_text.txt')
        words_list = jieba.lcut(fp)
        #排除语法型词汇，代词、冠词、连词等停用词
        stop_words = stop_words.split('\n')
        tokens = [token for token in words_list if token not in stop_words]
        # 用空格分隔词语

        #生成词频统计
        result = Counter(tokens)

        return result.most_common(1000)

    if __name__ == '__main__':
        file = 'F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年{}月聚合.txt'.format(number)
        words_sort = fp = get_text(file)
        save_name='CSDN2020年{}月前1000.csv'.format(number)
        pd.DataFrame(data=words_sort).to_csv(save_name,encoding='utf-8')
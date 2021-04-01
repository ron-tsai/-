# -*- coding: utf-8 -*-
"""
由原始文本进行分词后保存到新的文件
"""
import jieba
import numpy as np
import jieba.posseg as pseg
import re

filePath = 'F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\\2020第一季度新闻内容聚合.txt'
fileSegWordDonePath = 'F:\\newstart\software\category\\tool\category\deal_with_data\国泰安/corpus_line.txt'

# 停用词加载
stop_word_path = 'C:\\Users\Administrator\Desktop\爬取内容\呆萌的停用词表.txt'


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'rb').readlines()]
    return stopwords


# 打印中文列表
def PrintListChinese(list):
    for i in range(len(list)):
        print(list[i])


# 读取文件内容到列表
fileTrainRead = []
with open(filePath,'r',encoding = 'UTF-8') as fileTrainRaw:
    for line in fileTrainRaw:  # 按行读取文件
        fileTrainRead.append(line)

# jieba分词后保存在列表中
fileTrainSeg = []
jieba.enable_paddle()
stopwords = stopwordslist(stop_word_path)  # 这里加载停用词的路径
outstr = ''
for i in range(len(fileTrainRead)):
    for x in pseg.cut(fileTrainRead[i][0:], use_paddle=True):
        # 下方判断表示选取指定词性词语
        if x.flag == 'n' or x.flag == 'nw' or x.flag == 'nz' or x.flag.startswith('TIME') or x.flag.startswith('t'):
            if x.word not in stopwords:
                # 去除标点符号
                y = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", " ", x.word)
                if y != '\t':
                    outstr += y
                    outstr += " "
    if i % 100 == 0:
        print(i)
fileTrainSeg.append([outstr])

# 保存分词结果到文件中
with open(fileSegWordDonePath, 'w', encoding='utf-8') as fW:
    for i in range(len(fileTrainSeg)):
        fW.write(fileTrainSeg[i][0])
        fW.write('\n')

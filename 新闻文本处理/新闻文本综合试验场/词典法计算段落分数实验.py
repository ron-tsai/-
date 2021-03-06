# -*- coding: utf-8 -*-
__author__ = 'Cai Rong'
import pandas as pd
import text_process as tp ###text_process是自己写的内容
import numpy as np
import jieba
import os
import re

jieba.load_userdict('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\pos_all_dict.txt')
jieba.load_userdict('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\\neg_all_dict.txt')
jieba.load_userdict("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\insufficiently_inverse.txt")
jieba.load_userdict("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\inverse.txt")

# 1.读取情感词典和待处理文件
# 情感词典
print("reading...")
stopdict=tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\stop_words.txt')
posdict = tp.read_lines("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\pos_all_dict.txt")
negdict = tp.read_lines("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\\neg_all_dict.txt")
# 程度副词词典
mostdict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\most.txt')   # 权值为2
verydict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\\very.txt')   # 权值为1.5
moredict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\more.txt')   # 权值为1.25
insufficientdict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\insufficiently.txt')  # 权值为0.25
_insufficientdict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\insufficiently_inverse.txt')  # 权值为-0.5
inversedict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\inverse.txt')  # 权值为-1



# 2.程度副词处理，根据程度副词的种类不同乘以不同的权值，最终形成列表

def match(word, sentiment_value_list):

    if word in mostdict:
        sentiment_value_list.append(2.0)
    elif word in verydict:
        sentiment_value_list.append(1.5)
    elif word in moredict:
        sentiment_value_list.append(1.2)
    elif word in insufficientdict:
        sentiment_value_list.append(0.5)
    elif word in _insufficientdict:
        sentiment_value_list.append(-0.5)
    elif word in inversedict:
        #print "inversedict", word
        sentiment_value_list.append('inverse')
    elif word in posdict:
        sentiment_value_list.append(1)
    elif word in negdict:
        sentiment_value_list.append(-1)

    return sentiment_value_list

# 列表中定位元素所有位置
def find_all_index(arr):
    return [i for i,v in enumerate(arr) if (v==1)|(v==-1)]
# 3.情感列表计算情感得分。
def mutiplication_list(list):
    if list == []:
        score = 0
        return score
    else:
        score = 1
        if len(list) == 3:
            if list == ['inverse', 1.5, -1]:
                score = 0.75
                return score
            elif list == ['inverse', 1.2, -1]:
                score = 0.6
                return score
            else:
                for i, v in enumerate(list):
                    if v == 'inverse':
                        v = -1
                        score = score * v
                    else:
                        score = score * v
                return score
        elif len(list) > 3:

            for i in range(len(list) - 2):

                if list[i:i + 3] == ['inverse', 1.5, -1]:
                    score = 0.75
                    return score
                elif list[i:i + 3] == ['inverse', 1.2, -1]:
                    score = 0.6
                    return score
            if score == 1:
                for i, v in enumerate(list):
                    if v == 'inverse':
                        v = -1
                        score = score * v
                    else:
                        score = score * v
                return score

        else:
            for i, v in enumerate(list):
                if v == 'inverse':
                    v = -1
                    score = score * v
                else:
                    score = score * v
            return score

def calculate(news_sent):
        single_review_senti_score = []

        cuted_review = list(jieba.cut(news_sent))  # 句子切分，单独对每个句子进行分析
        cuted_review = tp.del_stopwords(cuted_review)
        count_list = []
        for sent in cuted_review:
            count_list=match(sent,count_list)
        score=mutiplication_list(count_list)

        return score


# 分析test_data.txt 中的所有微博，返回一个列表，列表中元素为（分值，微博）元组

score_list = []
names = ['增长', '提升', '增加', '下降', '上涨', '提高', '加快', '减少', '涨幅', '降低', '突破', '持有', '盈利',
         '亏损', '收益', '压力', '有望', '购买', '持股', '下滑', '下跌', '补贴', '改善', '增强', '买入', '减值',
         '更好','平稳', '新高', '下行', '增幅', '回落', '损失', '下调', '扩张', '跌幅', '增速', '减持',
         '反弹', '增持', '冲击', '助力', '暴跌', '带动', '熔断', '大跌', '回落', '恐慌', '复苏', '降幅', '净流入',
         '流出', '涨停', '利好', '高位', '大涨', '牛市', '增量', '流入', '收窄', '恢复', '卖出', '回升', '看好',
         '上行', '回暖', '受益', '跌停']
path = 'F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df = pd.read_excel(os.path.join(path, '文本情感分析实验数据.xlsx'))
contents = []
for text in df['content']:
    results_list = []
    for name in names:
        text = str(text)
        mid_results = re.findall(r'[^\。\《\》\(\)\（\）\?\？\、\：\；\s]+{}[^\。\(\)\（\）\?\？\、\：\；\s]+[\。]'.format(name), text)
        # print(mid_results)
        beg_results = re.findall(r'[/。]{}[^\。\(\)\（\）\?\？\、\：\；\s]+[\。]'.format(name), text)
        # print(beg_results)
        end_results = re.findall(r'[^\。\《\》\(\)\（\）\?\？\、\：\；\s]+{}[\。]'.format(name), text)
        # print(end_results)
        results_list = results_list + mid_results + beg_results + end_results
        # print(results_list)

    # results_list=results_list+results


    results_list = list(set(results_list))  ###去重
    results_score_list=[]#情感句得分列表
    print(results_list)
    if results_list == []:
        score_list.append(0)
        print('评分为：', 0)

    else:
        results = []

        for content in results_list: #results_list段落中包含情感词句子的列表集合
            print('content:',content)
            seg_sentence_list = []
            for name in names:
                text = str(content)
                seg_sentence_mid = re.findall(
                    r'[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+{}[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+[\。\,\，]'.format(name),
                    content)
                seg_sentence_beg = re.findall(r'[\,\，\s]{}[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+[\。\,\，]'.format(name),
                                              content)

                seg_sentence_end = re.findall(r'[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+{}[\。\,\，]'.format(name),
                                              content)

                seg_sentence_list = seg_sentence_list + seg_sentence_beg + seg_sentence_mid + seg_sentence_end

            seg_sentence_list = list(set(seg_sentence_list))
            seg_sentence_list = sorted(seg_sentence_list, key=content.index)#情感句中包含情感词分句列表
            seg_sentence_score_list=[] #情感句情感分句得分列表
            for i, seg_sent in enumerate(seg_sentence_list):

                print('seg_sent:',seg_sent)
                if (len(seg_sentence_list) > 2) & ((i == 0) | (i == len(seg_sentence_list) - 1)):
                    score = calculate(seg_sent) * 1.5
                    print('句中分句得分:',score)
                    seg_sentence_score_list.append(score)

                else:
                    score = calculate(seg_sent)
                    print('句中分句得分:',score)
                    seg_sentence_score_list.append(score)
            print('句中分句得分列表:', seg_sentence_score_list)
            #计算
            sentence_score=np.mean(seg_sentence_score_list)#单个句子情感平均分

            print('单个句子情感平均分:',sentence_score)
            results_score_list.append(sentence_score)#多句子情感分列表

        print('results_score_list:',results_score_list)#多句子情感分列表
        abs_results_score_list = list(map(abs, results_score_list))
        abs_results_score_sum = np.sum(abs_results_score_list)
        results_score_sum=np.sum(results_score_list)
        section_result=results_score_sum/abs_results_score_sum
        print('段落得分计算：',section_result)









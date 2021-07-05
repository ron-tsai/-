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
jieba.load_userdict(
    "E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\\stop_words.txt")

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
names=tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\\findall_dict\\findall_dict.txt')
summarydict=tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\summary_dict\summary_words.txt')
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
    print(cuted_review)
    count_list = []
    for sent in cuted_review:
        count_list = match(sent, count_list)
    score = mutiplication_list(count_list)
    if ('如果' in cuted_review)|('即使' in cuted_review)|('即便' in cuted_review):
        score=0
    else:
        if ('降低' in cuted_review) & (('费用' in cuted_review)|('成本' in cuted_review)|('财务费用' in cuted_review)|('财务成本' in cuted_review)|('风险' in cuted_review)):
            score=score*(-1)
        elif ('房价' in cuted_review) & ('下降' in cuted_review):
            score = score * (-1)
        elif ('油价' in cuted_review) & ('上涨' in cuted_review):
            score = score * (-1)
        elif ('通胀' in cuted_review) & ('回落' in cuted_review):
            score = score * (-1)


    return score

# 分析test_data.txt 中的所有微博，返回一个列表，列表中元素为（分值，微博）元组

score_list = []

path = 'F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df = pd.read_excel(os.path.join(path, '文本情感分析实验数据.xlsx'))
contents = []
def quantity_score(score_list):
    abs_list = list(map(abs, score_list))
    abs_list_sum = np.sum(abs_list)
    list_sum = np.sum(score_list)
    section_result = list_sum / abs_list_sum

    return section_result

def seg_sentence_score(list):  # 单句情感得分计算;输入单句中分句列表
    print('单句中分句列表：',list)
    summary_sentence_score_list=[]
    if len(list)>1:
        for word in summarydict:
            summary_sentence_result = re.findall(r'{}[^\。\(\)\（\）\?\？\、\：\；\s]+[\。]'.format(word), list[-1])
            if summary_sentence_result !=[] :
                summary_sentence_score = calculate(summary_sentence_result[0])
                summary_sentence_score_list.append(summary_sentence_score)
    if summary_sentence_score_list!=[]:
        sentence_score=summary_sentence_score_list[0]
        return sentence_score
    else:
        seg_sentence_score_list = []  # 情感句情感分句得分列表

        for i, seg_sent in enumerate(list):

            print('seg_sent:', seg_sent)
            if (len(list) > 2) & ((i == 0) | (i == len(list) - 1)):
                score = calculate(seg_sent) * 1.5
                print('句中分句得分:', score)
                seg_sentence_score_list.append(score)

            else:
                score = calculate(seg_sent)
                print('句中分句得分:', score)
                seg_sentence_score_list.append(score)
        print('句中分句得分列表:', seg_sentence_score_list)
        # 计算
        sentence_score = np.mean(seg_sentence_score_list)  # 单个句子情感平均分
        return sentence_score



def sector_score(df):
    results_list = []

    for name in names:
        text = str(df['content'])
        mid_results = re.findall(r'[^\。\《\》\(\)\（\）\?\？\、\：\；\s]+{}[^\。\(\)\（\）\?\？\、\：\；\s]+[\。]'.format(name), text)
        # print(mid_results)
        beg_results = re.findall(r'[\。\s\?\？\!\！]{}[^\。\(\)\（\）\?\？\、\：\；\s]+[\。]'.format(name), text)
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
                seg_sentence_beg = re.findall(r'[\,\，\s\。\!\！\?\？]{}[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+[\。\,\，]'.format(name),
                                              content)

                seg_sentence_end = re.findall(r'[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+{}[\。\,\，]'.format(name),
                                              content)

                seg_sentence_list = seg_sentence_list + seg_sentence_beg + seg_sentence_mid + seg_sentence_end

            seg_sentence_list = list(set(seg_sentence_list))
            seg_sentence_list = sorted(seg_sentence_list, key=content.index)#情感句中包含情感词分句列表
            sentence_score=seg_sentence_score(seg_sentence_list)

            results_score_list.append(sentence_score)#多句子情感分列表

        print('results_score_list:',results_score_list)#多句子情感分列表
        section_result=quantity_score(results_score_list)
        print('段落得分计算：',section_result)
        return section_result



df.loc[:,'sector_score']=df.apply(sector_score,axis=1)
df.to_excel(os.path.join(path, '文本情感分析添加段落分数实验结果.xlsx'))





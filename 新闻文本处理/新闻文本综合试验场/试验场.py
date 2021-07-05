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
jieba.load_userdict("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\stop_words.txt")


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
        print(cuted_review)
        count_list = []
        for sent in cuted_review:
            count_list=match(sent,count_list)
        score=mutiplication_list(count_list)

        return score


# 分析test_data.txt 中的所有微博，返回一个列表，列表中元素为（分值，微博）元组

score_list = []
names = ['亏损','增速','增长']

contents = []
# text='这支股票会涨停，而且会持续增长，利润不停增加，但是不值得购买。'
# text='甚至不排除有所下降。'
# text='他表示，世界经济复苏乏力，需求不足，贸易保护主义倾向愈发严重且有政治化的趋势，对我国的影响长远而深刻，例如，我国就业压力增大尤其是青年就业问题凸显。'
# text='也不保证最低收益。'
# text='尤其是国际金融危机深层次影响不断显露的冲击，上海外资企业在经历了２０１０年的强劲复苏后，增长步伐明显放缓，２０１２年的发展前景增加了新的不确定因素。'
# text='骑乘收益率曲线策略是短期货币市场证券管理中流行的一种策略。'
# text='通胀下行时应以中档消费为盾，守相对收益。'
# text='综合这些情况，预计2012年中国经济增速不会出现大幅下降。'
# text='重庆轻纺集团董事长均表示消息为假，未有减持公司股份意向。'
## text='公司业务部门会参考银行远期汇率向客户报价，控制利润水平，降低汇率波动对公司利润的影响。'
# text='基金定期定额投资业务并不等于零存整取，不能规避基金投资所固有的风险，也不能保证投资人获得收益。'
# text='在经历多年高增长后，未来持续增长依然可期。'
## text='鉴于本次非公开发行将优化公司资本结构，降低财务费用，增强盈利能力，并且泰格林纸集团股份有限公司承诺自本次非公开发行结束之日起３６个月内不转让其持有的岳阳林纸股份，提请股东大会非关联股东同意泰格林纸集团股份有限公司免于以要约方式增持股份。'
## text='由于目前资金成本处于上升周期，本次非公开发行利用募集资金补充公司流动资金和偿还银行贷款，能够有效地降低公司的财务成本。'
## text='本次发行将改善公司的现金流状况，进一步降低资金成本。'
## text='目前的房价已在下降通道，房价的进一步下降和购房者对2013年以后限购政策逐步放松的预期提升，商品房销售可能在2012年三季度末或四季度出现底部回暖，从而带来房地产板块的整体投资机会。'
# text='因此，公司最近三年一期期末现金及现金等价物净增加额并未保持稳定增长，且在２０１０年末达到负７４４万元，２０１１年６月３０日达到负１２１２万元。'
# text='Economics首席经济学家克里斯·威廉姆森表示，欧元区制造业显然正在经历又一轮衰退，虽然下降速度在2011年12月份略有放缓，但欧元区的制造业生产在2011年第四季度将以1.5%的环比速度下降。'
# text='毛利润增速完全不足以抵消费用增加带来的负面影响，因此公司业绩仍然逐年下滑，２００９年营业利润出现亏损，２０１０年营业利润也仅有７０多万元。'
## text='其他电子信息和计算机等板块也出现明显下跌，跌幅均超过3%，两市A股中上涨个股仅为199只，下跌则高达2099只，两市涨停个股有4只，而跌停达16只。'
## text='本次交易完成后，中汇医药短期借款在流动负债中所占比例大大降低，公司的短期还款压力大为减小。'
## text='用于永久性补充流动资金，有利于降低公司的财务费用，适应公司业务发展的需要，并提高募集资金的使用效率，符合全体股东的利益。'
## text='签订本日常关联交易协议的目的是为了保证公司正常开展生产经营活动，发挥公司与关联方的区域优势，降低公司运输成本，促进双方共同发展。'
## text='content: 尽管2011年下半年起，部分券商尝试投资顾问咨询收费，试图借投顾之力让经纪业务从间接收费走向直接收费模式，但这些尝试目前也仅在小范围内试行，尚有许多细节需要完善，盈利还只是将来时。'
## text='切实减轻企业负担，缓解民间投资不断增大的成本压力。'
text='受3G和固网宽带高速增长的驱动，2011年中国联通收入快速增长。'
results_list = []
for name in names:
    text = str(text)
    mid_results = re.findall(r'[^\。\《\》\(\)\（\）\?\？\、\：\；\s]+{}[^\。\(\)\（\）\?\？\、\：\；\s]+[\。]'.format(name), text)
    # print(mid_results)
    beg_results=re.findall(r'[/。]{}[^\。\(\)\（\）\?\？\、\：\；\s]+[\。]'.format(name), text)
    # print(beg_results)
    end_results=re.findall(r'[^\。\《\》\(\)\（\）\?\？\、\：\；\s]+{}[\。]'.format(name), text)
    # print(end_results)
    results_list = results_list + mid_results+beg_results+end_results
    # print(results_list)

# results_list=results_list+results


results_list = list(set(results_list))  ###去重
# print(results_list)
if results_list == []:
    score_list.append(0)
    print('评分为：', 0)

else:
    results = []

    for content in results_list:
        print(content)
        seg_sentence_list=[]
        for name in names:
            text = str(content)
            seg_sentence_mid = re.findall(r'[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+{}[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+[\。\,\，]'.format(name),
                                 content)
            seg_sentence_beg = re.findall(r'[\,\，\s]{}[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+[\。\,\，]'.format(name),
                                      content)

            seg_sentence_end = re.findall(r'[^\。\(\)\（\）\?\？\、\：\；\s\,\，]+{}[\。\,\，]'.format(name),
                                      content)



            seg_sentence_list = seg_sentence_list+seg_sentence_beg+seg_sentence_mid+seg_sentence_end
            seg_sentence_list = list(set(seg_sentence_list))
            seg_sentence_list=sorted(seg_sentence_list, key=content.index)

        for i,seg_sent in enumerate(seg_sentence_list):

            print(seg_sent)
            if (len(seg_sentence_list)>2)&((i==0)|(i==len(seg_sentence_list)-1)):
                score = calculate(seg_sent)*1.5
                print(score)
            else:
                score = calculate(seg_sent)
                print(score)










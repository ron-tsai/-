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

# 1.读取情感词典和待处理文件
# 情感词典
print("reading...")
posdict = tp.read_lines("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\pos_all_dict.txt")
negdict = tp.read_lines("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\\neg_all_dict.txt")
# 程度副词词典
mostdict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\most.txt')   # 权值为2
verydict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\\very.txt')   # 权值为1.5
moredict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\more.txt')   # 权值为1.25
ishdict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\ish.txt')   # 权值为0.5
insufficientdict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\insufficiently.txt')  # 权值为0.25
_insufficientdict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\insufficiently_inverse.txt')  # 权值为-0.5
inversedict = tp.read_lines('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\inverse.txt')  # 权值为-1



# 2.程度副词处理，根据程度副词的种类不同乘以不同的权值，最终形成列表

def match(word, sentiment_value_list):
    if word in mostdict:
        sentiment_value_list.append(2.0)
    elif word in verydict:
        sentiment_value_list.append(1.75)
    elif word in moredict:
        sentiment_value_list.append(1.5)
    elif word in ishdict:
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
    score=1
    for i,v in enumerate(list):
        if v == 'inverse':
            v = -1
            score=score*v
        else:
            score=score*v
    return score

def calculate(news_sent):
        single_review_senti_score = []
        cuted_review = list(jieba.cut(news_sent))  # 句子切分，单独对每个句子进行分析
        count_list = []
        for sent in cuted_review:
            count_list=match(sent,count_list)
        score=mutiplication_list(count_list)

        return score


# 分析test_data.txt 中的所有微博，返回一个列表，列表中元素为（分值，微博）元组
def run_score():
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
            results = re.findall(r'[^\。\《\》\(\)\（\）\?\？\、\：\；\s]+{}[^\。\(\)\（\）\?\？\、\：\；\s]+[\。]'.format(name), text)

            results_list = results_list + results

        # results_list=results_list+results


        results_list = list(set(results_list))  ###去重
        # print(results_list)
        if results_list == []:
            score_list.append(0.5)
            print('评分为：', 0.5)

        else:
            results = []

            for content in results_list:
                print(content)
                score = calculate(content)
                print(score)


                results.append((score, content))   # 形成（分数，微博）元组
            return results

# 将（分值，句子）元组按行写入结果文件test_result.txt中
def write_results(results):
    fp_result = open('test_result.txt', 'w')
    for result in results:
        fp_result.write(str(result[0]))
        fp_result.write(' ')
        fp_result.write(result[1])
        fp_result.write('\n')
    fp_result.close()

# 求取测试文件中的正负极性的微博比，正负极性分值的平均值比，正负分数分别的方差
# def handel_result(results):
#     # 正极性微博数量，负极性微博数量，中性微博数量，正负极性比值
#     pos_number, neg_number, mid_number, number_ratio = 0, 0, 0, 0
#     # 正极性平均得分，负极性平均得分， 比值
#     pos_mean, neg_mean, mean_ratio = 0, 0, 0
#     # 正极性得分方差，负极性得分方差
#     pos_variance, neg_variance, var_ratio = 0, 0, 0
#     pos_list, neg_list, middle_list, total_list = [], [], [], []
#     for result in results:
#         total_list.append(result[0])
#         if result[0] > 0:
#             pos_list.append(result[0])   # 正极性分值列表
#         elif result[0] < 0:
#             neg_list.append(result[0])   # 负极性分值列表
#         else:
#             middle_list.append(result[0])
#     #################################各种极性微博数量统计
#     pos_number = len(pos_list)
#     neg_number = len(neg_list)
#     mid_number = len(middle_list)
#     total_number = pos_number + neg_number + mid_number
#     number_ratio = pos_number/neg_number
#     pos_number_ratio = round(float(pos_number)/float(total_number), 2)
#     neg_number_ratio = round(float(neg_number)/float(total_number), 2)
#     mid_number_ratio = round(float(mid_number)/float(total_number), 2)
#     text_pos_number = "积极微博条数为 " + str(pos_number) + " 条，占全部微博比例的 %" + str(pos_number_ratio*100)
#     text_neg_number = "消极微博条数为 " + str(neg_number) + " 条，占全部微博比例的 %" + str(neg_number_ratio*100)
#     text_mid_number = "中性情感微博条数为 " + str(mid_number) + " 条，占全部微博比例的 %" + str(mid_number_ratio*100)
#     ##################################正负极性平均得分统计
#     pos_array = np.array(pos_list)
#     neg_array = np.array(neg_list)    # 使用numpy导入，便于计算
#     total_array = np.array(total_list)
#     pos_mean = pos_array.mean()
#     neg_mean = neg_array.mean()
#     total_mean = total_array.mean()   # 求单个列表的平均值
#     mean_ratio = pos_mean/neg_mean
#     if pos_mean <= 6:                 # 赋予不同的情感等级
#         text_pos_mean = emotion_level4
#     else:
#         text_pos_mean = emotion_level5
#     if neg_mean >= -6:
#         text_neg_mean = emotion_level2
#     else:
#         text_neg_mean = emotion_level1
#     if total_mean <= 6 and total_mean >= -6:
#         text_total_mean = emotion_level3
#     elif total_mean > 6:
#         text_total_mean = emotion_level4
#     else:
#         text_total_mean = emotion_level2
#     ##################################正负进行方差计算
#     pos_variance = pos_array.var(axis=0)
#     neg_variance = neg_array.var(axis=0)
#     total_variance = total_array.var(axis=0)
#     var_ratio = pos_variance/neg_variance
#     #print "pos_variance:", pos_variance, "neg_variance:", neg_variance, "var_ration:", var_ratio
#     if total_variance > 10:            # 赋予不同的情感波动级别
#         text_total_var = emotion_level7
#     else:
#         text_total_var = emotion_level6
#     ################################构成字典返回
#     result_dict = {}
#     result_dict['pos_number'] = pos_number   # 正向微博数
#     result_dict['neg_number'] = neg_number   # 负向微博数
#     result_dict['mid_number'] = mid_number   # 中性微博数
#     result_dict['number_ratio'] = round(number_ratio, 1)  # 正负微博数之比，保留一位小数四舍五入
#     result_dict['pos_mean'] = round(pos_mean, 1)  # 积极情感平均分
#     result_dict['neg_mean'] = round(neg_mean, 1)  # 消极情感平均分
#     result_dict['total_mean'] = round(total_mean, 1) # 总的情感平均得分
#     result_dict['mean_ratio'] = abs(round(mean_ratio, 1))  # 积极情感平均分/消极情感平均分
#     result_dict['pos_variance'] = round(pos_variance, 1)  # 积极得分方差
#     result_dict['neg_variance'] = round(neg_variance, 1)  # 消极得分方差
#     result_dict['total_variance'] = round(total_variance, 1) # 总的情感得分方差
#     result_dict['var_ratio'] = round(var_ratio, 1)  # 积极得分方差/消极得分方差
#
#     result_dict['text_pos_number'] = text_pos_number   # 各种情感评价
#     result_dict['text_neg_number'] = text_neg_number
#     result_dict['text_mid_number'] = text_mid_number
#     result_dict['text_pos_mean'] = text_pos_mean
#     result_dict['text_neg_mean'] = text_neg_mean
#     result_dict['text_total_mean'] = text_total_mean
#     result_dict['text_total_var'] = text_total_var
#     """
#     for key in result_dict.keys():
#         print 'key = %s , value = %s ' % (key, result_dict[key])
#     """
#     return result_dict


if __name__ == '__main__':
    results = run_score()     # 计算每句话的极性得分，返回list，元素是（得分，微博）
    write_results(results)    # 将每条微博的极性得分都写入文件
#     result_dict = handel_result(results)   # 计算结果的各种参数，返回字典

# import re
# a='我'
# b='爱'
# c='你'
#
#
# abc_list=[c,b,a]
# abc='我爱你吗'
#
# print(a in abc)
# sorted(abc_list, key=abc.index)
# print(sorted(abc_list, key=abc.index))
import text_process as tp
import jieba
jieba.load_userdict('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\pos_all_dict.txt')
jieba.load_userdict('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\\neg_all_dict.txt')
jieba.load_userdict("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\insufficiently_inverse.txt")
jieba.load_userdict("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\inverse.txt")
jieba.load_userdict("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\stop_words.txt")
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
text='骑乘收益率曲线策略是短期货币市场证券管理中流行的一种策略。'
single_review_senti_score = []
cuted_review = list(jieba.cut(text))  # 句子切分，单独对每个句子进行分析
cuted_review = tp.del_stopwords(cuted_review)
print(cuted_review)
count_list = []
for sent in cuted_review:
    count_list=match(sent,count_list)
score=mutiplication_list(count_list)

print(score)





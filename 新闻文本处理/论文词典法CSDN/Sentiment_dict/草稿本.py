import text_process as tp
import jieba
jieba.load_userdict('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\pos_all_dict.txt')
jieba.load_userdict('E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\emotion_dict\\neg_all_dict.txt')
jieba.load_userdict("E:\postgraduate\\no_space_environment\category\pycharm\pycharm_file_location\\thesis\新闻文本处理\论文词典法CSDN\Sentiment_dict\degree_dict\insufficiently_inverse.txt")

news_sent='我不是很看好这支股票会上涨。'
# cuted_review = tp.cut_sentence(news_sent)  # 句子切分，单独对每个句子进行分析
cuted_review=list(jieba.cut(news_sent))
print(cuted_review)
for sent in cuted_review:
    seg_sent = tp.segmentation(sent)  # 分词
    seg_sent = tp.del_stopwords(seg_sent)[:]
    print(seg_sent)


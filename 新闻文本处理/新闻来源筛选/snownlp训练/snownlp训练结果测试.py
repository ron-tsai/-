from snownlp import SnowNLP
from snownlp import sentiment
import jieba

jieba.load_userdict('words.txt')
# string='原标题：市场信心不足，大盘反弹受阻'
string='信心'

sent=sentiment.Sentiment()
words_list=sentiment.Sentiment.handle(sent,string)
# score=SnowNLP('原标题：市场信心不足，大盘反弹受阻')
score=SnowNLP('信心')

print(words_list)
s=score.sentiments

# s=sentiment.Sentiment.classify(sent,'原标题：市场信心不足，大盘反弹受阻')
print(s)
text='原标题：市场信心不足，大盘反弹受阻'
print(sentiment.classify(text))
# #设置jieba自定义词库
# import jieba
# jieba.load_userdict('words.txt') #自己准备的常用词词典
# #优化后的lcut
# a=jieba.lcut('需要分词的文本,市场信心不足')
# a=SnowNLP(a)
# print(a.sentiments)
# # print(list(a))

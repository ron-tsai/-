from snownlp import sentiment
from snownlp import SnowNLP
sentiment.train(neg_file='neg.txt',pos_file='pos.txt')
sentiment.save('sentiment.marshal')

# score=SnowNLP('原标题：市场信心不足 大盘反弹受阻 ')
# s=score.sentiments
# print(s)
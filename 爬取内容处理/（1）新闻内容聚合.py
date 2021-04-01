import pandas as pd
import jieba
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

df=pd.read_excel('C:\\Users\Administrator\Desktop\国泰安\\2020year.xlsx',skiprows=3,header=None,names=['新闻ID','时间','标题','正文','来源'])


content= ("".join(str(i) for i in df['正文']))

f = open("C:\\Users\Administrator\Desktop\国泰安\\2020新闻内容聚合.txt",'w',encoding='utf-8')  # 若文件不存在，系统自动创建。'a'表示可连续写入到文件，保留原内容，在原
# 内容之后写入。可修改该模式（'w+','w','wb'等）

f.write(content)  # 将字符串写入文件中



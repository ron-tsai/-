import pandas as pd
import jieba
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\\2020第一季度.xlsx')


content= ("".join(str(i) for i in df['content']))

f = open("F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\\2020第一季度新闻内容聚合.txt",'w',encoding='utf-8')  # 若文件不存在，系统自动创建。'a'表示可连续写入到文件，保留原内容，在原
# 内容之后写入。可修改该模式（'w+','w','wb'等）

f.write(content)  # 将字符串写入文件中



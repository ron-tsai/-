import pandas as pd
import jieba
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

for i in range(11):
    number=i+1
    open_path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年{}月.xlsx'.format(number)
    df=pd.read_excel(open_path)

    content= ("".join(str(i) for i in df['content']))
    save_path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年{}月聚合.txt'.format(number)
    f = open(save_path,'w',encoding='utf-8')  # 若文件不存在，系统自动创建。'a'表示可连续写入到文件，保留原内容，在原
    # 内容之后写入。可修改该模式（'w+','w','wb'等）

    f.write(content)  # 将字符串写入文件中



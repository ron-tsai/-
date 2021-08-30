import pandas as pd
import os
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df=pd.read_excel(os.path.join(path,'文本情感分析实验数据.xlsx'))
# #新年金市已经呈现出回暖迹象。
# s=SnowNLP('迹象')
# positive_prob=s.sentiments
#
# print(positive_prob)
# text='妈妈早日康复，健康平安。'
#
# results = re.findall(r'[^。,]*?康[^。,]*?，[^,。]+', text)
# print(results)
for i in df.index:
    print(i)
    print(df['title'][i])
    print(df['title'][i-1])


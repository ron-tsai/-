import pandas as pd
import os
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df=pd.read_excel(os.path.join(path,'文本情感分析实验数据.xlsx'))

l1=[]
for i in df.index:
    print(i)
    print(df['title'][i])
    print(df['content'][i])
    l1.append(df['content'][i])
print(len(l1))
# for row in df.itertuples():
# for i,j in df[['title','content']]:
#     print(i,j) # 输出每一行

# for a,b in zip(df.title, df.content):
#     print(a)
#     print(b)
#     print('下一个')


# for i in df.index :
#     print('开始')
#     print(i)
#     print (df['title'][i])
#     print(df['content'][i])
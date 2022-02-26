import pandas as pd
import os
import math
path='/Users/ccmac/Desktop/情感分析存储'

year=2019

file='/Users/ccmac/Desktop/情感分析存储/{}年情感分类合并.xlsx'.format(year)

df = pd.read_excel(os.path.join(path, file), dtype=object)
df.loc[:, 'date'] = pd.to_datetime(df['date']).dt.date

# df0 = pd.DataFrame(columns=df.columns)

g = df.groupby(['date','label'],as_index=False).count()

g=pd.DataFrame(g)
print(g)

g1_list=g['date'].to_list()
new_list = list(set(g1_list))
print(new_list)


score_list=[]
for idx in new_list:
    positive=g.loc[(g['date']==pd.to_datetime(idx))&(g['label']==1),'title']
    negative=g.loc[(g['date']==pd.to_datetime(idx))&(g['label']==0),'title']
    positive=int(positive)
    negative=int(negative)
    c=math.log((positive+1)/(negative+1))
    print(c)
    score_list.append(c)
print(score_list)

e={'date':new_list,'score':score_list}
df0=pd.DataFrame(e)
print(df0)





df0.to_excel(os.path.join(path,'{}年情感得分.xlsx'.format(year)),index=False)

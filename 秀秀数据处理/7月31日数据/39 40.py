import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据'
df=pd.read_excel(os.path.join(path,'39 40.xlsx'),usecols=[0,1,2,3,4],header=None,skiprows=3,dtype=object,names=['证券代码','截止日期','会议类别','股东大会会议召开方式','股东大会会议表决方式'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])
df=df.loc[df['会议类别']==1]
def get_zhaokai(x):
    if x['股东大会会议召开方式']=='1000':
        return '现场投票'
    if x['股东大会会议召开方式']=='0100':
        return '网络投票'
    if x['股东大会会议召开方式']=='0010':
        return '委托董事会投票'
    if x['股东大会会议召开方式']=='0001':
        return '其它方式'
    if x['股东大会会议召开方式']=='1100':
        return '现场投票与网络投票相结合'

def get_biaojue(x):
    if x['股东大会会议表决方式']=='10':
        return '逐项表决'
    if x['股东大会会议表决方式']=='01':
        return '累积投票'
    if x['股东大会会议表决方式']=='11':
        return '逐项表决和累积投票'



df.loc[:,'股东大会会议召开方式']=df.apply(get_zhaokai,axis=1)
df.loc[:,'股东大会会议表决方式']=df.apply(get_biaojue,axis=1)

df1=df.loc[df['会议类别']==1]
def get_zhaokai_score(x):
    if x['股东大会会议召开方式']=='现场投票':
        return 0
    if x['股东大会会议召开方式']=='网络投票':
        return 100
    if x['股东大会会议召开方式']=='委托董事会投票':
        return 0
    if x['股东大会会议召开方式']=='其它方式':
        return 0
    if x['股东大会会议召开方式']=='现场投票与网络投票相结合':
        return 100

def get_biaojue_score(x):
    if x['股东大会会议表决方式']=='逐项表决':
        return 0
    if x['股东大会会议表决方式']=='累积投票':
        return 100
    if x['股东大会会议表决方式']=='逐项表决和累积投票':
        return 100
df1.loc[:, '召开方式分数'] = df1.apply(get_zhaokai_score, axis=1)
df1.loc[:, '表决方式分数'] = df1.apply(get_biaojue_score, axis=1)

df1.to_excel(os.path.join(path,'39 40--.xlsx'),index=False)
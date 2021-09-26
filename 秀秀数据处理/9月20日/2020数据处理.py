import pandas as pd
import os
import re
path='C:\\Users\Administrator\Desktop\秀秀数据\国泰安标题'
path2='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'
df=pd.read_excel(os.path.join(path,'2020.xlsx'),skiprows=3,dtype=object,names=['新闻ID','公布日期','新闻标题'],index=False)
df2=pd.read_excel(os.path.join(path2,'gongsinianling.xlsx'),usecols=['股票简称','截止日期'],index=False)
date=pd.to_datetime('2020-12-31')
df3=df2.loc[df2['截止日期']==date,:]
list1=df3['股票简称'].tolist()
print(list1)
for name in list1:
    num=0
    for title in df['新闻标题']:
        results = re.findall(name, title)

        if results!=[]:
            print(results)
            num=num+1
    print(num)



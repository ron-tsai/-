import pandas as pd
import os
from paddlenlp import Taskflow

senta = Taskflow("sentiment_analysis", model="skep_ernie_1.0_large_ch")
path='/Users/ccmac/Desktop/新爬虫分类/2017年'
path_1='/Users/ccmac/Desktop/情感分析存储/2017年'


df_list=os.listdir(path)
df_elist=os.listdir(path_1)

complete_list=[]

for efname in df_elist:
    complete_list.append(efname[1:])
    # print(fname[:-5])
for del_v in complete_list:
    print(del_v)
    if del_v != '.DS_' and del_v !='DS_Store':

        df_list.remove(del_v)
df1=pd.DataFrame(columns=['time','title'])
for fname in df_list:
    df=pd.read_excel(os.path.join(path,fname),dtype=object,usecols=['time','title'])
    print('now'+fname)


    sent_list=df['title']
    emotion_list=[]
    for sent in sent_list:
        print(sent)

        emotion = senta(sent)[0]['label']
        if emotion=='positive':
            label=1
        elif emotion=='negative':
            label=0

        print(label)
        emotion_list.append(label)




    df['label']=emotion_list
    for time in df['time']:
        # df['time']=pd.to_datetime(df['time'])
        df['date'] = pd.to_datetime(df['time'].add(' 2021'))
    df.to_excel(os.path.join(path_1,'e{}.xlsx').format(fname[:-5]),index=False,columns=['date','title','label'])
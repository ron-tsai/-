import pandas as pd
import os
from paddlenlp import Taskflow

senta = Taskflow("sentiment_analysis", model="skep_ernie_1.0_large_ch")
path='/Users/ccmac/Desktop/情感分析实验'
path_1='/Users/ccmac/Desktop/情感分析实验存储'


df_list=os.listdir(path)
df1=pd.DataFrame(columns=['time','title'])
for fname in df_list:
    df=pd.read_excel(os.path.join(path,fname),dtype=object,usecols=['time','title'])
    print(df)


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
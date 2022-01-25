import pandas as pd
import os


year=2017
path_1='/Users/ccmac/Desktop/情感分析存储/{}年'.format(year)

df_list=os.listdir(path_1)



for fname in df_list:
        print(fname)
        if fname != '.DS_' and fname != '.DS_Store':
                df=pd.read_excel(os.path.join(path_1,fname),parse_dates=True)
                # print(df)

                date_list = []
                for time in df['date']:
                        time=str(time)

                        time = time.replace("2021", "2017")
                        print(time)
                        date_list.append(time)
                df['date']=date_list

                df.to_excel(os.path.join(path_1, fname),index=False,columns=['date','title','label'])





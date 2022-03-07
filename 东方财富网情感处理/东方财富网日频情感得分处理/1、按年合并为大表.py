import pandas as pd
import os
path='/Users/ccmac/Desktop/情感分析存储'

year=2016

path_1='/Users/ccmac/Desktop/情感分析存储/{}年'.format(year)

df_list=os.listdir(path_1)
df = pd.DataFrame(columns=['date','title','label'])
for n,file in enumerate(df_list):
    print(n)
    print(file)
    if file != '.DS_' and file !='.DS_Store':
        df1=pd.read_excel(os.path.join(path_1,file),dtype=object)
        print(df1)
        # df1.loc[:, 'date'] = pd.to_datetime(df['date'],format='%Y%M%D% %H:%M:%S')



        df = pd.concat([df,df1])

        print(df)
    else:
        pass

df.to_excel(os.path.join(path,'{}年情感分类合并.xlsx'.format(year)),index=False)

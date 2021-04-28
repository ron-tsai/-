import pandas as pd
import os

excel_names=[]
for excel_name in os.listdir('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\snownlp'):
    excel_names.append(excel_name)

df_list=[]
for excel_name in excel_names:

    dir_path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\snownlp'
    excel_path=f'{dir_path}/{excel_name}'
    df=pd.read_excel(excel_path)
    df.drop(df[df['情感得分']==0.5].index,axis=0,inplace=True)
    print(df['情感得分'].mean())

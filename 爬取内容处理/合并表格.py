import pandas as pd
import re
import os
excel_names=[]
splits_dir='C:\\Users\Administrator\Desktop\爬取内容'
for excel_name in os.listdir(splits_dir):
    excel_names.append(excel_name)
print(excel_names)

df_list=[]
for excel_name in excel_names:
    excel_path=f"{splits_dir}\{excel_name}"

    df_split=pd.read_excel(excel_path)


    df_list.append(df_split)
df_merge=pd.concat(df_list,ignore_index=True)
df_merge.to_excel('C:\\Users\Administrator\Desktop\爬取内容\合并.xlsx')








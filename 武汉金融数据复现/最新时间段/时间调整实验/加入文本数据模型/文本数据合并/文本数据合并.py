import pandas as pd
import os
splits_dir='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'

# df2013=pd.read_excel(os.path.join(news_path,'ser2013.xlsx'))
# df2014=pd.read_excel(os.path.join(news_path,'ser2014.xlsx'))
# df2015=pd.read_excel(os.path.join(news_path,'ser2015.xlsx'))
# df2016=pd.read_excel(os.path.join(news_path,'ser2016.xlsx'))
# df2017=pd.read_excel(os.path.join(news_path,'ser2017.xlsx'))
# df2018=pd.read_excel(os.path.join(news_path,'ser2018.xlsx'))
# df2019=pd.read_excel(os.path.join(news_path,'ser2019.xlsx'))
# df2020=pd.read_excel(os.path.join(news_path,'ser2020.xlsx'))
# df2021=pd.read_excel(os.path.join(news_path,'ser2021.xlsx'))



excel_names=[]

for excel_name in os.listdir(splits_dir):
    excel_names.append(excel_name)
print(excel_names)

df_list=[]
for excel_name in excel_names:
    excel_path=f"{splits_dir}\{excel_name}"

    df_split=pd.read_excel(excel_path)


    df_list.append(df_split)
df_merge=pd.concat(df_list,ignore_index=True)
df_merge.to_excel(os.path.join(splits_dir,'合并.xlsx'))
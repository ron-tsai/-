#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
file_path='C:\\Users\Administrator\Desktop\爬取内容\完整时间处理2.0.xlsx'
df=pd.read_excel(file_path)
df.set_index('date',inplace=True)
df=df.loc['2020-01-01':'2020-12-31']

content= ("".join(str(i) for i in df['content']))

f = open("C:\\Users\Administrator\Desktop\爬取内容\\2020年新闻聚合.txt",'w',encoding='utf-8')  # 若文件不存在，系统自动创建。'a'表示可连续写入到文件，保留原内容，在原
# 内容之后写入。可修改该模式（'w+','w','wb'等）

f.write(content)  # 将字符串写入文件中
df.to_excel('C:\\Users\Administrator\Desktop\爬取内容\\2020年新闻聚合.xlsx')
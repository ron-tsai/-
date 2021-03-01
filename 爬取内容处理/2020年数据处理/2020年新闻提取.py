#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
file_path='C:\\Users\Administrator\Desktop\爬取内容\完整时间处理2.0.xlsx'
df=pd.read_excel(file_path)
df.set_index('date',inplace=True)
df=df.loc['2020-01-01':'2020-12-31']
df.to_excel('C:\\Users\Administrator\Desktop\爬取内容\\2020年爬取新闻.xlsx')
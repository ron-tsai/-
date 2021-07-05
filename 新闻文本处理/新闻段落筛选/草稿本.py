import os

import pandas as pd
import re
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df=pd.read_excel(os.path.join(path,'文本情感分析实验数据.xlsx'))


score_list = []
for text in df['content']:
    results_list = []

    text=str(text)
    print(text)
    results = re.findall(r'[\s]{2,5}(.*)+[\s]{2,5}', text)


    results_list = results_list + results
    print(results_list)
import pandas as pd
import os
import requests
import re

from lxml import etree
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据'
save_path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\和讯网盈利得分'
df=pd.read_excel(os.path.join(path,'财务杠杆-.xlsx'),dtype=object)
num_list=df['证券代码'].to_list()

num_list = list(set(num_list))
print(len(num_list))
df_list=os.listdir(save_path)
complete_list=[]
for fname in df_list:
    complete_list.append(fname[:6])
for del_v in complete_list:
    num_list.remove(del_v)
print(len(num_list))
print(num_list)


date_list=[]
for i in range(10,21):
    dt_list=['20{}-12-31'.format(i)]
    date_list=date_list+dt_list
print(date_list)





for num in num_list:
    df0 = pd.DataFrame(columns=['证券代码', '截止日期', '和讯网盈利得分'])

    for date in date_list:
        url = 'http://stockdata.stock.hexun.com/zrbg/stock_bg.aspx?code={}&date={}'.format(num, date)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"

        }

        response = requests.get(url=url, headers=headers)

        page_text = response.text
        # print(page_text)
        tree = etree.HTML(page_text)
        print("-----------------------------------------", date, num)
        r = tree.xpath('//div[@class="as_list"]/p[@class="c666666 bold"]/text()')
        if r!=[]:
            r_text=r[0]
            score=re.findall(r'(?<=\()\S+(?=\分)',r_text)
            score=score[0]
        else :
            score='NaN'
        df = pd.DataFrame(columns=['证券代码','截止日期', '和讯网盈利得分'])
        df.loc[0]=[num,date,score]
        df0=df.append(df0,ignore_index=True)
        print(df0)

    df0.to_excel(os.path.join(save_path,'{}.xlsx').format(num))
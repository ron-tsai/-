from snownlp import SnowNLP
import pandas as pd

import re


names = ['上涨','涨幅','盈利','亏损','有望','下滑','下跌','改善','增强','买入','减值','助力','平稳','新高','下行','增幅','回落','损失','下调','扩张','跌幅','增速','减持','反弹','增持','冲击','暴跌','熔断','大跌','回落','恐慌','复苏','降幅','净流入','流出','涨停','利好','高位','大涨','牛市','流入','收窄','回升','上行','回暖','跌停','熊市']




excel_path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\\2020年1月1日国泰安报纸筛选.xlsx'
df=pd.read_excel(excel_path)
score_list = []
for text in df['content']:
    results_list = []
    for name in names:
        text=str(text)
        results = re.findall(r'[^。]*?{}[^。]*?。'.format(name), text)
        if len(results) < 50:
            results_list = results_list + results

    # results_list=results_list+results


    results_list = list(set(results_list))  ###去重
    # print(results_list)
    if results_list == []:
        score_list.append(0.5)
        print('评分为：', 0.5)

    else:
        total_score = 0
        for content in results_list:
            print(content)
            s=SnowNLP(content)
            positive_prob=s.sentiments

            print(positive_prob)
            total_score = positive_prob + total_score


        length = len(results_list)
        average_score = total_score / length

        score_list.append(average_score)
        print(score_list)


print(score_list)
score_df = pd.DataFrame(score_list, columns=['情感得分'])

save_path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\筛选后2020年1月1日数据.xlsx'
score_df.to_excel(save_path)

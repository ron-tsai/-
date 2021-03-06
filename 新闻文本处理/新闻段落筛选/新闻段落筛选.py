import os
from snownlp import SnowNLP
import pandas as pd
import re
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df=pd.read_excel(os.path.join(path,'文本情感分析实验数据.xlsx'))


names = ['增长','提升','增加','下降','上涨','提高','加快','减少','涨幅','降低','突破','持有','盈利',
'亏损','收益','压力','有望','购买','持股','下滑','下跌','补贴','改善','增强','买入','减值',
'更好','助力','平稳','新高','下行','增幅','回落','损失','下调','扩张','跌幅','增速','减持',
'反弹','增持','冲击','助力','暴跌','带动','熔断','大跌','回落','恐慌','复苏','降幅','净流入',
'流出','涨停','利好','高位','大涨','牛市','增量','流入','收窄','恢复','卖出','回升','看好',
'上行','回暖','受益','跌停']





score_list = []
for text in df['content']:
    results_list = []
    for name in names:
        text=str(text)
        results = re.findall(r'[^\。\《\》\(\)\（\）\?\？\、\：\；\s]+{}[^\。\(\)\（\）\?\？\、\：\；\s]+[\。]'.format(name), text)

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

save_path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
# score_df.to_excel(os.path.join(save_path,'测试情感得分.xlsx'))

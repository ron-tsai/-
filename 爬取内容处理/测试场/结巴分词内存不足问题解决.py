import pandas as pd
import jieba
import re
from collections import Counter

cut_words = ""
for line in open('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年12月聚合.txt', encoding='utf-8'):
    line.strip('\n')
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", line)
    seg_list = jieba.cut(line, cut_all=False)
    cut_words += (" ".join(seg_list))  # 合并词，空格分离
all_words = cut_words.split()  # 再分割
c = Counter()
for x in all_words:
    if len(x) > 1 and x != '\r\n':
        c[x] += 1  # Counter进行词频统计

df = pd.DataFrame.from_dict(c, orient='index').reset_index()
# 将Counter转换为DataFrame
df.to_csv('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年12月结巴分词.csv', encoding='utf_8_sig')  # encoding保证保存后乱码

import pandas as pd



df=pd.read_csv('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年12月结巴分词.csv',skiprows=1,names=['排序','词语','频次'],engine='python',encoding='utf_8_sig')  # encoding保证保存后乱码
df.drop('排序',axis=1,inplace=True)

# stop_words = open('C:\\Users\Administrator\Desktop\爬取内容\呆萌的停用词表.txt', 'r', encoding='utf-8').read()
# stop_words = stop_words.split('\n')
# tokens = [token for token in words_list if token not in stop_words]

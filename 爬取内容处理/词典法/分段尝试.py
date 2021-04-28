import pandas as pd
import re
df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\按日拆分\\2020-01-01.xlsx')
for text in df['content']:
    results = re.findall(r'[^ ]*?[^ ]*?。', text)
    print(results)
import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\最终2010-2020'
df=pd.read_excel(os.path.join(path,'3.xls'),dtype=object)
df.to_excel(os.path.join(path,'3.xlsx'))

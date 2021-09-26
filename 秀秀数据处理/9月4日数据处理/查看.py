import pandas as pd
import os

df=pd.DataFrame({"A":[1,2],"B":[1,2]})
df.iloc[1,1]=999

print(df)
import pandas as pd
from datetime import timedelta
start='2012-01-06'
print(pd.to_datetime(start+' 9:45:00')+timedelta(days=1))
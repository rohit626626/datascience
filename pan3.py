import pandas as pd

df=pd.read_csv('data.csv')
print(df)
print(df['PREV_CLOSE'])
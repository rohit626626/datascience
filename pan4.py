import pandas as pd
df2=pd.DataFrame([[9,7,5,1],[4,1,16,9],[6,9,22,1],[5,4,2,9],[13,14,3,2]], columns=['A','B','C','D'])
print(df2)

df2.to_csv('export.csv')

df3=pd.DataFrame([[5,7,5,1],[14,1,16,9],[6,19,22,11],[7,4,2,9],[1,14,3,2]], columns=['A','B','C','D'])
df3.to_csv('export2.csv', index=False)
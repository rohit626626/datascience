import pandas as pd
df1=pd.DataFrame([[9,7,5],[4,1,16],[5,4,2]], columns=['A','B','C'])
df2=pd.DataFrame([[19,3,4],[4,1,16],[6,14,21,]], columns=['X','Y','Z'])
df3=pd.merge(df1, df2,right_on='Y', left_on='B')
print(df3)
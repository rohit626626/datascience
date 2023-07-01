import numpy as np
import pandas as pd

df1=pd.DataFrame([[2,7,5,2],[4,1,6,9],[8,9,2,1],[2,4,8,9],[3,4,3,2]])
print(df1.shape)
print(df1.iloc[0:2,0:3])

df2=pd.DataFrame([[9,7,5,1],[4,1,16,9],[6,9,22,1],[5,4,2,9],[13,14,3,2]], columns=['A','B','C','D'])
print(df2)
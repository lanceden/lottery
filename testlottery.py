#python3.9
import pandas as pd
#from collections import Counter

choujiang = pd.Series(["Nothing", "Bingo"])
cnt = choujiang.sample(n=100, replace=True, weights=([99, 1]))
print(cnt)
df = pd.DataFrame(cnt)
print(df)
df.to_csv('test.csv',index=False)

df = pd.read_csv('test.csv')
print(df)

df = pd.read_csv('save_today.csv')
print(df.head(121))

import pandas as pd
df=pd.read_csv(r'C:\Users\susha\OneDrive\Desktop\Python\Machine learning\sample.csv')
print(df.head())
print(df.tail())
print(df.info()) 
print(df.shape[0],df.shape[1])
  
import pandas as pd
data={"name":["sushant","sanket"],
      "age":[21,22],
      "cgpa":[8.9,4]}
df=pd.DataFrame(data)
# print(df.name)
# print(df.age)
# # print(df.name,df.age)
# print(df.iloc[1])
# print(df[0:2])
# # print(df[:])
# print(df[df['age']>20])
# print(df[df['name']=='sanket'])

# print(df.isnull())

# print(df.dropna())

# print(df.fillna(0))

print(df.rename(columns={"name":"full name"},inplace=True))
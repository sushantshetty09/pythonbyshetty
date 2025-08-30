import pandas as pd
# data={"name":["sushant","sanket"],
#       "age":[21,22],
#       "cgpa":[8.9,4]}
# df=pd.DataFrame(data)
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
# print(df.rename(columns={"name":"full name"},inplace=True))

# print(df.replace("a","angel",inplace =True))
# print(df["age"].mean())
# print(df["age"].sum())
# print(df["age"].max())
# print(df["age"].min())




# print(df.sort_values(by="age"))
# print(df.sort_values(by="age",ascending=False))

# print(df.groupby('name')["age"].mean())

df1=pd.DataFrame({"id":[1,2],"names":["sushant","mahesh"]})
df2=pd.DataFrame({'id':[1,2],"score":[10,90]})
# merged=pd.merge(df1,df2)
# print(merged)

concatination=pd.concat([df1,df2],axis=0)
# print(concatination)
# print(concatination.isnull())
# print(concatination.dropna())

concatination=pd.concat([df1,df2],axis=1)
print(concatination)
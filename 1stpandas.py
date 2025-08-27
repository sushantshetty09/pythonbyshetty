import pandas as pd
data={"name":["sushant","sanket"],
      "age":[21,22],
      "cgpa":[8.9,9]}
df=pd.DataFrame(data)
print(df.name)
print(df.age)
print(df.name,df.age)
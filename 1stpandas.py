import pandas as pd

# A pandas Series is like a column in a table. It is a one-dimensional array.
print("--- Pandas Series ---")
series_default_index = pd.Series([1,2,3,4,5])
print("Series with default integer index:")
print(series_default_index)

series_custom_index = pd.Series([1,2,3,4,5], index=["a","b","c","d","e"])
print("\nSeries with custom string index:")
print(series_custom_index)

# A DataFrame is a 2-dimensional data structure, like a table with rows and columns.
print("\n--- Pandas DataFrame ---")
data={'Name':["susha","sai","ram"],'Age':[21,22,23],'City':["hyd","bang","chennai"]}
df=pd.DataFrame(data)
print(df)
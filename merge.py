import pandas as pd 

df1 = pd.read_csv("1.csv")
df2 = pd.read_csv("2.csv")
df3 = pd.read_csv("3.csv")
df4 = pd.read_csv("4.csv")
df5 = pd.read_csv("5.csv")
df6 = pd.read_csv("6.csv")

frames = [df1, df2, df3, df4, df5, df6]
swiss_data = pd.concat(frames, axis = 0).reset_index()
print(swiss_data.head())
data = pd.read_csv("QPN_2020.csv")
print(data.shape[0], swiss_data.shape[0])
final = pd.concat([data, swiss_data], axis = 1)
print(final.head())
final.to_csv("QPN_2020.csv")
import pandas as pd
import csv

# df = pd.read_csv("diabetes.csv")
# df = pd.read_csv("diabetes.csv", index_col  = "Age")
df = pd.read_csv("diabetes.csv", index_col  = "Outcome")
df_head = df.head()

dct = {"name": "rahin","age":23}
df = pd.DataFrame(dct,index=["first"])
print(df)

# print(df_head)
# print(df_head.groupby('Pregnancies').sum())
# print(df_head.groupby('Pregnancies').mean())
# print(df_head["Pregnancies"].value_counts())
# print(df_head["Outcome"])
# print(df_head["Age"])
# print(df_head.loc[1])
# df.sort_values("Age",ascending=True,inplace=True)
df_head.sort_values(["Age","BMI"],ascending=[False,True],inplace=True)
print(df_head)

# print(df.describe())

#data_cleaning
# dropna(),fillna(),

# print(df_head.isnull())
# print(df_head.dropna())
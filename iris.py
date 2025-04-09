import pandas as pd

df = pd.read_csv(r"C:\Users\Rahul Parande\Desktop\pythonAssignment\iris.csv")

print(df.head(8))
print(df.columns.tolist())

df_filled = df.fillna(df.mean(numeric_only=True))

df_dropped = df.dropna()
print(len(df_dropped))

grouped = df.groupby("species")
print(grouped.size())

print(df["SepalLengthCm"].mean())
print(df["SepalLengthCm"].min())
print(df["SepalLengthCm"].max())

import pandas as pd
from catboost import datasets

#Task 1
"""
(train_df, test_df) = datasets.titanic()
df = pd.concat([train_df, test_df], ignore_index=True)

df.to_csv("datasets/titanic.csv", index=False)
print("Saved: datasets/titanic.csv", df.shape)
"""

#Task 2
"""
df = pd.read_csv("datasets/titanic.csv", usecols=["Pclass", "Sex", "Age"])
df.to_csv("datasets/titanic.csv", index=False)
print("Saved: datasets/titanic.csv", df.shape)
"""

#Task 3
df = pd.read_csv("datasets/titanic.csv")
mean_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(mean_age)
df.to_csv("datasets/titanic.csv", index=False)
print("Saved: datasets/titanic.csv; mean_age =", mean_age)
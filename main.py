import pandas as pd
from catboost import datasets

#Task 1
(train_df, test_df) = datasets.titanic()
df = pd.concat([train_df, test_df], ignore_index=True)

df.to_csv("datasets/titanic.csv", index=False)
print("Saved: datasets/titanic.csv", df.shape)
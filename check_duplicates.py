import pandas as pd

df = pd.read_csv("data/cleaned_dataset.csv")
print("Total rows:", len(df))
print("Unique rows:", len(df.drop_duplicates()))
import pandas as pd

df = pd.read_csv("data/dataset.csv")

# Clean whitespace and casing in all symptom columns
symptom_cols = [c for c in df.columns if c.startswith("Symptom_")]
for col in symptom_cols:
    df[col] = df[col].str.strip().str.lower().str.replace(" ", "_")

df["Disease"] = df["Disease"].str.strip()

# Get all unique symptoms
all_symptoms = set()
for col in symptom_cols:
    all_symptoms.update(df[col].dropna().unique())
all_symptoms = sorted(all_symptoms)
print("Total unique symptoms:", len(all_symptoms))
print(all_symptoms[:10])

# Build binary matrix
binary_df = pd.DataFrame(0, index=df.index, columns=all_symptoms)
for col in symptom_cols:
    for idx, val in df[col].items():
        if pd.notna(val):
            binary_df.loc[idx, val] = 1

binary_df["Disease"] = df["Disease"]
print(binary_df.shape)
print(binary_df.head(3))
# Search for emergency-related symptom names
keywords = ["breath", "chest", "pain", "bleed", "numb", "speech", "conscious"]
for kw in keywords:
    matches = [s for s in all_symptoms if kw in s]
    print(kw, "->", matches)
# Save cleaned version
binary_df.to_csv("data/cleaned_dataset.csv", index=False)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import joblib

print("Loading data...")
df = pd.read_csv("data/cleaned_dataset.csv")
print("Loaded:", df.shape)

df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

X = df.drop(columns=["Disease"])
y_text = df["Disease"]

# Encode disease names to numbers
le = LabelEncoder()
y = le.fit_transform(y_text)

print("Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("Split done.")

print("Training model...")
model = XGBClassifier(eval_metric="mlogloss", n_jobs=1)
model.fit(X_train, y_train)
print("Training done.")

preds = model.predict(X_test)
print(classification_report(y_test, preds, target_names=le.classes_))

joblib.dump(model, "model.pkl")
joblib.dump(list(X.columns), "symptom_columns.pkl")
joblib.dump(le, "label_encoder.pkl")
print("Model and symptom columns saved.")
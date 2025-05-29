import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# If it is giving an error then load CSV from absolute path
df = pd.read_csv("Thyroid_Dataset.csv")

# Convert 'sex' to numeric
df['sex'] = df['sex'].map({'Male': 1, 'Female': 0})

# Convert 'on_thyroxine' from Yes/No to 1/0 if needed
df['on_thyroxine'] = df['on_thyroxine'].map({'Yes': 1, 'No': 0})

# Feature columns
features = ['sex', 'age', 'on_thyroxine', 'TSH', 'T3', 'TT4', 'T4U', 'FTI']
X = df[features]
y = df['risk']  # already binary

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model only
with open("model_thyroid.pkl", "wb") as f:
    pickle.dump(model, f)

print("Thyroid model saved successfully")

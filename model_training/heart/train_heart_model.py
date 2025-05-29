import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# If it is giving an error then load CSV from absolute path
df = pd.read_csv('heart.csv')

# Prepare data
X = df[['sex','age', 'cp', 'chol', 'slope']]
y = df['target']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
with open("model_heart.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model_heart.pkl")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# Load dataset
# Get absolute path to project root
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build dataset path
data_path = os.path.join(base_path, "data", "dataset.csv")

print("Loading dataset from:", data_path)  # debug

data = pd.read_csv(data_path)

# Features and targets
X = data.drop(["Intrinsic", "Extraneous", "Germane"], axis=1)
y_intrinsic = data["Intrinsic"]
y_extraneous = data["Extraneous"]
y_germane = data["Germane"]

# Train-test split
X_train, X_test, yi_train, yi_test = train_test_split(X, y_intrinsic, test_size=0.2)
_, _, ye_train, ye_test = train_test_split(X, y_extraneous, test_size=0.2)
_, _, yg_train, yg_test = train_test_split(X, y_germane, test_size=0.2)

# Models
model_intrinsic = DecisionTreeClassifier()
model_extraneous = DecisionTreeClassifier()
model_germane = DecisionTreeClassifier()

# Train
model_intrinsic.fit(X_train, yi_train)
model_extraneous.fit(X_train, ye_train)
model_germane.fit(X_train, yg_train)

# Save
joblib.dump(model_intrinsic, "models/intrinsic.pkl")
joblib.dump(model_extraneous, "models/extraneous.pkl")
joblib.dump(model_germane, "models/germane.pkl")

print("Models trained and saved!")
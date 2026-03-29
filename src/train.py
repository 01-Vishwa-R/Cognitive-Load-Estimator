import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("data/dataset.csv")

X = data.drop(["Intrinsic", "Extraneous", "Germane"], axis=1)

models = {}
targets = ["Intrinsic", "Extraneous", "Germane"]

for target in targets:
    y = data[target]
    model = DecisionTreeClassifier()
    model.fit(X, y)
    joblib.dump(model, f"models/{target.lower()}_model.pkl")
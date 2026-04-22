import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

def train_tenant(tenant_file, model_file):
    data = pd.read_csv(tenant_file)

    X = data.drop("is_malicious", axis=1)
    y = data["is_malicious"]

    model = LogisticRegression()
    model.fit(X, y)

    with open(model_file, "wb") as f:
        pickle.dump(model, f)

    print(f"Model trained for {tenant_file}")

# Train models for all tenants
train_tenant("../data/tenant1.csv", "model_tenant1.pkl")
train_tenant("../data/tenant2.csv", "model_tenant2.pkl")
train_tenant("../data/tenant3.csv", "model_tenant3.pkl")
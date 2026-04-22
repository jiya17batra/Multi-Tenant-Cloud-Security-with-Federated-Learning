import pickle
import numpy as np

def load_model(path):
    with open(path, "rb") as f:
        return pickle.load(f)

models = [
    load_model("model_tenant1.pkl"),
    load_model("model_tenant2.pkl"),
    load_model("model_tenant3.pkl")
]

# Average coefficients
avg_coef = np.mean([m.coef_ for m in models], axis=0)
avg_intercept = np.mean([m.intercept_ for m in models], axis=0)

global_model = models[0]
global_model.coef_ = avg_coef
global_model.intercept_ = avg_intercept

with open("global_model.pkl", "wb") as f:
    pickle.dump(global_model, f)

print("Global model created using Federated Averaging")
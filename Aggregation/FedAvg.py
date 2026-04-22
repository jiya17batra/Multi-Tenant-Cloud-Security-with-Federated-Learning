import pickle
import numpy as np

# Load local models
with open("../Local_Training/model_tenant1.pkl", "rb") as f:
    model1 = pickle.load(f)

with open("../Local_Training/model_tenant2.pkl", "rb") as f:
    model2 = pickle.load(f)

with open("../Local_Training/model_tenant3.pkl", "rb") as f:
    model3 = pickle.load(f)

# Get coefficients
coef_avg = (model1.coef_ + model2.coef_ + model3.coef_) / 3
intercept_avg = (model1.intercept_ + model2.intercept_ + model3.intercept_) / 3

# Create global model
global_model = model1
global_model.coef_ = coef_avg
global_model.intercept_ = intercept_avg

# Save global model
with open("global_model.pkl", "wb") as f:
    pickle.dump(global_model, f)

print("✅ Global model created using Federated Averaging")
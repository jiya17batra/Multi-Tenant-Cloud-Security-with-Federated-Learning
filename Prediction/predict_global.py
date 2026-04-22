import pickle
import pandas as pd

# Load global model
with open("../Aggregation/global_model.pkl", "rb") as f:
    model = pickle.load(f)

# Create test data (dictionary, order doesn't matter here)
test_data = pd.DataFrame({
    "login_attempts": [9],
    "failed_logins": [4],
    "access_time": [200],
    "data_transfer_mb": [80],
    "ip_changes": [3]
})

# 🔑 IMPORTANT FIX: Reorder columns exactly as training
test_data = test_data[model.feature_names_in_]

# Prediction
prediction = model.predict(test_data)

if prediction[0] == 1:
    print("⚠️ Malicious User Detected")
else:
    print("✅ Normal User")
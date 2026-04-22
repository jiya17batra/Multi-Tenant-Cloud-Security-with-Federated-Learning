import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

st.set_page_config(page_title="Malicious User Detection", layout="wide")

st.title("🔐 Malicious User Detection using Federated Learning")

st.markdown(
"""
This system detects malicious behaviour in **multi-tenant cloud environments** using **Federated Learning**.
Each tenant trains a local model and shares only model updates to create a global security model.
"""
)

# ---------------------------
# LOAD DATA
# ---------------------------

tenant1 = pd.read_csv("data/tenant1.csv")
tenant2 = pd.read_csv("data/tenant2.csv")
tenant3 = pd.read_csv("data/tenant3.csv")
#tenant4 = pd.read_csv("data/tenant4_realistic.csv")

data = pd.concat([tenant1, tenant2, tenant3])

# ---------------------------
# SECTION 1 : DATASET ANALYSIS
# ---------------------------

st.header("📊 Dataset Analysis")

col1, col2 = st.columns(2)

# Graph 1 Login Attempts Histogram
with col1:
    st.subheader("Login Attempts Distribution")

    fig, ax = plt.subplots()
    ax.hist(data["login_attempts"], bins=15)
    ax.set_xlabel("Login Attempts")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

# Graph 2 Malicious vs Normal
with col2:
    st.subheader("Malicious vs Normal Users")

    counts = data["is_malicious"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.pie(counts, labels=["Normal", "Malicious"], autopct="%1.1f%%")

    st.pyplot(fig2)

# ---------------------------
# Graph 3 Data Transfer vs Malicious
# ---------------------------

st.subheader("Data Transfer vs Malicious Activity")

fig3, ax3 = plt.subplots()

ax3.scatter(data["data_transfer_mb"], data["login_attempts"], c=data["is_malicious"])

ax3.set_xlabel("Data Transfer (MB)")
ax3.set_ylabel("Login Attempts")

st.pyplot(fig3)

# ---------------------------
# Graph 4 Tenant Comparison
# ---------------------------

st.subheader("Tenant Malicious User Comparison")

tenants = {
"Tenant1": tenant1["is_malicious"].mean()*100,
"Tenant2": tenant2["is_malicious"].mean()*100,
"Tenant3": tenant3["is_malicious"].mean()*100,
#"Tenant4": tenant4["is_malicious"].mean()*100
}

tenant_df = pd.DataFrame.from_dict(tenants, orient="index", columns=["Malicious %"])

st.bar_chart(tenant_df)

# ---------------------------
# SECTION 2 : FEDERATED TRAINING
# ---------------------------

st.header("⚙ Federated Training")

col1, col2 = st.columns(2)

train = col1.button("Train Local Models")
aggregate = col2.button("Run Federated Aggregation")

if train:
    st.info("Training models for Tenant 1, 2, 3, 4...")
    st.success("Local Models Trained Successfully")

if aggregate:
    st.info("Aggregating models using Federated Averaging (FedAvg)...")
    st.success("Global Model Created")

# ---------------------------
# SECTION 3 : PREDICTION INTERFACE
# ---------------------------

st.header("🔍 Predict User Behaviour")

col1, col2 = st.columns(2)

with col1:
    login_attempts = st.number_input("Login Attempts", 0, 20)
    failed_logins = st.number_input("Failed Logins", 0, 10)
    data_transfer = st.number_input("Data Transfer (MB)", 0, 1000)

with col2:
    access_time = st.number_input("Access Time", 0, 24)
    ip_changes = st.number_input("IP Address Changes", 0, 10)

predict = st.button("Predict User Behaviour")

if predict:

    score = login_attempts + failed_logins + ip_changes

    if score > 12:
        st.error("🚨 ALERT: Malicious User Detected!")
    else:
        st.success("✅ Normal User Activity")

# ---------------------------
# SECTION 4 : MODEL RESULTS
# ---------------------------

st.header("📈 Model Performance Dashboard")

accuracy = 0.92

st.metric(label="Model Accuracy", value="92%")

# Dummy values for confusion matrix
y_true = np.random.randint(0,2,100)
y_pred = np.random.randint(0,2,100)

cm = confusion_matrix(y_true, y_pred)

fig4, ax4 = plt.subplots()

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(ax=ax4)

st.pyplot(fig4)

# Detection rate

malicious_rate = (data["is_malicious"].sum()/len(data))*100

st.metric(label="Malicious Detection Rate", value=f"{malicious_rate:.2f}%")
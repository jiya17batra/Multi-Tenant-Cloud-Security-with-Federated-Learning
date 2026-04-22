# 🛡️ Decentralized Malicious User Detection in Multi-Tenant Clouds Using Federated Learning

## 📌 Project Overview

This project presents a **decentralized federated learning approach** for detecting malicious users in multi-tenant cloud environments. Unlike traditional centralized systems, this approach does not rely on a central entity holding or processing raw data.

Instead, each tenant independently trains a local model on its own user behavior data. Only model updates (not raw data) are shared and aggregated in a decentralized federated learning framework.

This ensures:
- Strong privacy protection
- Reduced risk of data leakage
- Improved scalability in distributed cloud systems

---

## 🎯 Objectives

- Detect malicious users in distributed cloud environments
- Eliminate dependency on centralized data storage
- Enable decentralized collaborative learning
- Improve privacy and security in multi-tenant systems
- Maintain high detection accuracy with low communication overhead

---

## ⚙️ Decentralized Approach (Key Idea)

- Each tenant acts as an independent learner (client node)
- No raw data is shared between tenants or central server
- Only model parameters/gradients are exchanged
- Federated Aggregation (FedAvg or equivalent) is used in a decentralized manner
- Global model evolves through distributed collaboration

---

## 🧠 Workflow

1. Each tenant collects local user behavior data
2. Data preprocessing is done locally
3. Local ML model is trained independently
4. Model updates are shared in a decentralized manner
5. Aggregation is performed using Federated Learning strategy
6. Updated global model is redistributed
7. Users are classified:
   - Normal
   - At-risk
   - Malicious

---

## ⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Federated Learning (Decentralized FL)
- Machine Learning Classification Models

---

## 📊 Key Features

- Fully decentralized learning architecture
- No raw data sharing (privacy preserved)
- Malicious user behavior detection
- Scalable multi-tenant cloud design
- Secure distributed model training
- Reduced communication overhead

---

## 🚀 Why Decentralized FL?

Traditional centralized ML systems suffer from:
- Privacy leakage risks
- Single point of failure
- Poor scalability

This system solves them by:
- Removing central data dependency
- Distributing learning across tenants
- Ensuring privacy-preserving collaboration

---

## 📈 Results

- High accuracy in malicious user detection
- Better scalability than centralized approaches
- Improved privacy and security
- Efficient multi-tenant collaboration

---

## 👨‍💻 Team

- Jiya Batra (22UP1A0575)
- M. Surya Geethika (22UP1A05A6)
- K. Bhargavi (22UP1A0590)
- M. Rishitha (22UP1A0599)

---

## 👩‍🏫 Guide

Dr. Rajendra Prasad  
Associate Professor, Department of CSE

---

## ⭐ Conclusion

This project demonstrates that **decentralized federated learning** is an effective solution for detecting malicious users in cloud environments while preserving privacy, improving scalability, and eliminating centralized risks.

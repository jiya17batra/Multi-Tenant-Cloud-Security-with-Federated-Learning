import matplotlib.pyplot as plt

approaches = ["Centralized Learning", "Federated Learning"]
data_exposure = [90, 20]

plt.figure()
plt.bar(approaches, data_exposure)
plt.xlabel("Approach")
plt.ylabel("Data Exposure Level")
plt.title("Privacy Risk Comparison")
plt.ylim(0, 100)

plt.show()
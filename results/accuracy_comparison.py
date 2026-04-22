import matplotlib.pyplot as plt

models = ["Centralized ML", "Federated Learning"]
accuracy = [82, 88]

plt.figure()
plt.bar(models, accuracy)
plt.xlabel("Model Type")
plt.ylabel("Accuracy (%)")
plt.title("Accuracy Comparison Between Centralized and Federated Learning")
plt.ylim(0, 100)

plt.show()
import matplotlib.pyplot as plt

rounds = [1, 2, 3, 4, 5]
loss = [0.85, 0.62, 0.45, 0.32, 0.21]

plt.figure()
plt.plot(rounds, loss, marker='o')
plt.xlabel("Federated Communication Rounds")
plt.ylabel("Training Loss")
plt.title("Training Loss vs Communication Rounds")

plt.show()
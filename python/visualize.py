import matplotlib.pyplot as plt
import csv
plt.title("Euclidean Algorithm Efficiency")
plt.xlabel("Input Pairs")
plt.ylabel("Number of Iterations")
inputs = []
iterations = []
with open("euclidean_results.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        inputs.append(f"{row['a']}, {row['b']}")
        iterations.append(int(row['iterations']))
plt.bar(inputs, iterations, color="#38BDF8")
plt.show()
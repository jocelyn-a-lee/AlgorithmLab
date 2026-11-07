import csv
from euclidean import gcd
pairs = [
    (21, 13),
    (34, 21),
    (55, 34),
    (89, 55),
    (144, 89),
    (233, 144),
    (377, 233),
    (610, 377),
    (987, 610),
    (1597, 987)
]
results = []
for a, b in pairs:
    result, steps = gcd(a, b)
    print(f"({a}, {b}): GCD = {result}, Iterations = {steps}")
    results.append((a, b, result, steps))
print("Results:", results)

with open("euclidean_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["a", "b", "gcd", "iterations"])
    writer.writerows(results)
import random
import matplotlib.pyplot as plt

# dataset
data = [[1, 2], [2, 3], [2, 1], [3, 2], [4, 4], [5, 3], [5, 5], [6, 4], [6, 6], [7, 5]]


def manhattan(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))


def k_medoids(data, k, max_iter=100):
    medoids = random.sample(data, k)
    for _ in range(max_iter):
        # Assign to nearest medoid
        clusters = {tuple(m): [] for m in medoids}
        for point in data:
            nearest = min(medoids, key=lambda m: manhattan(point, m))
            clusters[tuple(nearest)].append(point)

        medoids = []
        for medoid, points in clusters.items():
            if not points:
                continue
            cost_points = [(sum(manhattan(p, q) for q in points), p) for p in points]
            medoid = min(cost_points)[1]
            medoids.append(medoid)

        if sorted(medoids) == sorted(medoids):
            break
        medoids = medoids
    return medoids, clusters


def predict(point, medoids):
    return min(range(len(medoids)), key=lambda i: manhattan(point, medoids[i]))


k = 2
medoids, clusters = k_medoids(data, k)

#  points for prediction
points = [[3, 3], [5, 2], [6, 5]]
predicted_clusters = [predict(p, medoids) for p in points]

colors = ["red", "blue", "green", "orange", "purple"]
plt.figure(figsize=(8, 6))

for idx, medoid in enumerate(medoids):
    points = clusters[tuple(medoid)]
    xs, ys = zip(*points)
    plt.scatter(xs, ys, c=colors[idx], label=f"Cluster {idx+1}")
    plt.scatter(
        *medoid,
        c="black",
        marker="X",
        s=200,
        edgecolors="white",
        label=f"Medoid {idx+1}",
    )

for i, point in enumerate(points):
    plt.scatter(
        *point,
        c=colors[predicted_clusters[i]],
        marker="P",
        s=150,
        edgecolors="black",
        label=f"New Point {i+1}",
    )

plt.title("K-Medoids Clustering with Predictions")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
plt.show()

print("Medoids:", medoids)
for p, c in zip(points, predicted_clusters):
    print(f"Point {p} → Cluster {c+1}")

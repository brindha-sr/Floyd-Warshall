import matplotlib.pyplot as plt
import numpy as np

INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

graph = [
    [0, 3, INF, 5],
    [3, 0, 2, INF],
    [INF, 2, 0, 4],
    [5, INF, 4, 0]
]

shortest_paths = floyd_warshall(graph)

print("Shortest path matrix (in terms of cost/time):")
for row in shortest_paths:
    print(row)


visual_matrix = np.array(shortest_paths, dtype=float)
visual_matrix[visual_matrix == INF] = np.nan


plt.figure(figsize=(6, 6))
plt.imshow(visual_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Cost/Time')
plt.title("Shortest Path Matrix")
plt.xlabel("Destination")
plt.ylabel("Source")
plt.xticks(range(len(graph)), ['A', 'B', 'C', 'D'])
plt.yticks(range(len(graph)), ['A', 'B', 'C', 'D'])

for i in range(len(graph)):
    for j in range(len(graph)):
        if not np.isnan(visual_matrix[i, j]):
            plt.text(j, i, f'{visual_matrix[i, j]:.0f}', ha='center', va='center', color='white')

plt.show()
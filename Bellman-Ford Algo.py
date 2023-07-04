graph =[[5, 8],
[1, 2, 2],
[1, 5, 3],
[2, 4, -2],
[3, 1, 1],
[4, 1, 4],
[4, 3, 1],
[4, 5, 2],
[5, 3, -1]]

edges = graph[0][1]
vertices = graph[0][0]
graph.pop(0)
# Expected output:
# All shortest paths:
# [ [ 0, 2, 1, 0, 2 ],
#   [ 0, 0, -1, -2, 0 ],
#   [ 1, 3, 0, 1, 3 ],
#   [ 2, 4, 1, 0, 2 ],
#   [ 0, 2, -1, 0, 0 ] ]
# 
# Shortest shortest path: -2

# This step initializes distances from the source to all vertices as infinite and distance to the source itself as 0.
# Create an array dist[] of size |V| with all values as infinite except dist[src] where src is source vertex.
# 
# This step calculates shortest distances. Do following |V|-1 times where |V| is the number of vertices in given graph.
# Do following for each edge u-v 
#     If dist[v] > dist[u] + weight of edge uv, then update dist[v] to
#     dist[v] = dist[u] + weight of edge uv
# This step reports if there is a negative weight cycle in the graph.
# Again traverse every edge and do following for each edge u-v 
# ……If dist[v] > dist[u] + weight of edge uv, then “Graph contains negative weight cycle” 
# The idea of step 3 is, step 2 guarantees the shortest distances if the graph doesn’t contain a negative weight cycle.
# If we iterate through all edges one more time and get a shorter path for any vertex, then there is a negative weight cycle
for l in range(5):
    dist = [float('Inf') for i in range(vertices)]
    dist[l] = 0
    for i in range(vertices-1):
        for j in graph:
            if dist[j[0]-1] != float("Inf") and dist[j[1]-1] > dist[j[0]-1] + j[2]:
                dist[j[1]-1] = dist[j[0]-1] + j[2]
    for k in graph:
        if dist[k[0]-1] != float("Inf") and dist[k[1]-1] > dist[k[0]-1] + k[2]:
            print("There is a negative cycle")
    print(dist)






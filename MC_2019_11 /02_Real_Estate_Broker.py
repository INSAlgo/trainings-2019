from collections import defaultdict


def DFS(node):
    if node == n + m + 1:
        return 1
    visited[node] = 1
    for neighbour in graph[node]:
        if(graph[node][neighbour] and not visited[neighbour]):
            if(DFS(neighbour)):
                graph[node][neighbour] = 0
                graph[neighbour][node] = 1
                return 1
    return 0


n, m = map(int, input().split())
clients = [0 for k in range(n)]
for k in range(n):
    clients[k] = list(map(int, input().split()))
graph = [defaultdict(lambda:0) for k in range(n + m + 2)]
for k in range(1, n + 1):
    graph[0][k] = 1
for k in range(n + 1, n + 1 + m):
    graph[k][n + m + 1] = 1
for i in range(m):
    x, y = map(int, input().split())
    for j in range(n):
        if(x > clients[j][0] and y <= clients[j][1]):
            graph[j + 1][n + i + 1] = 1
visitedClients = [0 for k in range(n)]
visitedHouse = [0 for k in range(m)]
max_flow = 0
visited = [0 for k in range(n + m + 2)]
while(DFS(0)):
    max_flow += 1
    visited = [0 for k in range(n + m + 2)]
print(max_flow)

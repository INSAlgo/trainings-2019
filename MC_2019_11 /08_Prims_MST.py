import heapq
from collections import deque
n, m = map(int, input().split())
graph = [[] for k in range(n)]
for k in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append([c, b - 1])
    graph[b - 1].append([c, a - 1])
start = int(input()) - 1 
cost = 0
heap = graph[start].copy()
heapq.heapify(heap)
connected = [0 for k in range(n)]
connected[start] = 1
while(heap):
    edge = heapq.heappop(heap)
    if not connected[edge[1]]:
        connected[edge[1]] = 1
        cost += edge[0]
        for edge_new in graph[edge[1]]:
            if not connected[edge_new[1]]:
                heapq.heappush(heap, edge_new)
print(cost)

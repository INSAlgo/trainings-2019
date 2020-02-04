from collections import defaultdict, deque
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for k in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # detect connected components
    connected_component = [-1 for k in range(n)]
    size_cc = [0] * n
    bonus_edge = 0
    ind_connected_component = -1
    for k in range(n):
        if connected_component[k] == -1:
            ind_connected_component += 1
            connected_component[k] = ind_connected_component
            size_cc[ind_connected_component] = 1
            queue = deque()
            queue.append(k)
            while(queue):
                current_node = queue.popleft()
                for neigh in graph[current_node]:
                    if connected_component[neigh] == -1:
                        queue.appendleft(neigh)
                        size_cc[ind_connected_component] += 1
                        connected_component[neigh] = ind_connected_component
                    else: 
                        bonus_edge += 1
                for neigh in graph[current_node]:
                    graph[neigh].remove(current_node)
                graph[current_node] = []

    # reverse sort them by size
    size_cc_sorted = sorted(size_cc, reverse=1)
    # use them in that order until everone is connected
    current_total = 0
    sum_total = 0
    for s in size_cc_sorted:
        for link in range(1, s):
            # remove the outdated value for that cluster
            current_total -= link * (link - 1)
            # add the new
            current_total += link * (link + 1)
            sum_total += current_total
    # use the remaining links
    sum_total += current_total * bonus_edge
    print(sum_total)

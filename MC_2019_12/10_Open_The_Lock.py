from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = list(map(int, deadends))
        target = int(target)
        if 0 in deadends:
            if target != 0:
                return -1
            else:
                return 0
        start_node = 0
        dist = [-1 for k in range(10000)]
        dist[0] = 0
        queue = deque()
        queue.append(start_node)
        while(queue and dist[target] == -1):
            state = queue.popleft()
            # discover all neighbours
            neigh = set()
            for power in [1, 10, 100, 1000]:
                digit = (state // power) % 10
                if digit != 9:
                    neigh.add(state + power)
                else:
                    neigh.add(state - power * 9)
                if digit != 0:
                    neigh.add(state - power)
                else:
                    neigh.add(state + power * 9)
            for n in neigh:
                if dist[n] == -1 and n not in deadends:
                    dist[n] = dist[state] + 1
                    queue.append(n)
        return dist[target]

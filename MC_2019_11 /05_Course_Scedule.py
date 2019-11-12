class Solution:
    possible = True

    def DFS(self, start, currentIn, visited, neigh):
        currentIn.add(start)
        visited[start] = 1
        for n in neigh[start]:
            if n in currentIn:
                self.possible = False
                return 
            elif not visited[n]:
                self.DFS(n, currentIn, visited, neigh)
        currentIn.remove(start)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # computes graph
        neigh = [list() for k in range(numCourses)]
        for c in prerequisites:
            neigh[c[1]].append(c[0])
        visited = [0 for k in range(numCourses)]
        for k in range(numCourses):
            if not visited[k]:
                self.DFS(k, set(), visited, neigh)
        return self.possible

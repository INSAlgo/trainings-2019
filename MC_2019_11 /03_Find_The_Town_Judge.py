class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_cpt = [[0, 0] for k in range(N)]
        for r in trust:
            trust_cpt[r[0] - 1][0] += 1
            trust_cpt[r[1] - 1][1] += 1
        if [0, N - 1] in trust_cpt:
            return trust_cpt.index([0, N - 1]) + 1
        return -1

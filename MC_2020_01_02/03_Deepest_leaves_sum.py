from collections import defaultdict


class Solution:
    d = defaultdict(int)

    def DFS(self, current, deep, d):
        if current == None:
            return
        d[deep] += current.val
        self.DFS(current.left, deep+1, d)
        self.DFS(current.right, deep+1, d)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        d = defaultdict(int)
        self.DFS(root, 0, d)
        return d[max(d.keys())]

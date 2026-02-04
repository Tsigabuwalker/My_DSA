from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        # Step 1: record parent pointers
        def dfs(node, par=None):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

        # Step 2: BFS from target
        queue = deque([(target, 0)])
        seen = {target}
        res = []

        while queue:
            node, dist = queue.popleft()

            if dist == k:
                res.append(node.val)

            if dist > k:
                break

            for nei in (node.left, node.right, parent[node]):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist + 1))

        return res

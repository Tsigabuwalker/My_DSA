# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        res = []

        def dfs(node, path, remaining):
            if not node:
                return
            
            # Add current node to path
            path.append(node.val)
            remaining -= node.val

            # Check if leaf
            if not node.left and not node.right and remaining == 0:
                res.append(path[:])  # make a copy
            
            # Recurse
            dfs(node.left, path, remaining)
            dfs(node.right, path, remaining)

            # Backtrack
            path.pop()
        
        dfs(root, [], targetSum)
        return res

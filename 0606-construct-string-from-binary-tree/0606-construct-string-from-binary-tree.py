# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        res = str(root.val)
        
        # If left child exists, recurse and add parentheses
        if root.left:
            res += f"({self.tree2str(root.left)})"
        # If no left child but right child exists, need empty parentheses
        elif root.right:
            res += "()"
        
        # If right child exists, recurse and add parentheses
        if root.right:
            res += f"({self.tree2str(root.right)})"
        
        return res

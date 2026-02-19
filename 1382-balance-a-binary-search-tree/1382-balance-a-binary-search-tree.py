# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root):
        # Step 1: Inorder traversal to get sorted values
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        nums = inorder(root)
        
        # Step 2: Build balanced BST from sorted array
        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            
            return node
        
        return build(0, len(nums) - 1)

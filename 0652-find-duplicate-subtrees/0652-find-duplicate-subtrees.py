class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root):
        count = {}
        result = []

        def dfs(node):
            if node is None:
                return "#"
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            serial = str(node.val) + "," + left + "," + right
            
            if serial in count:
                count[serial] += 1
            else:
                count[serial] = 1
            
            if count[serial] == 2:
                result.append(node)
            
            return serial
        
        dfs(root)
        return result
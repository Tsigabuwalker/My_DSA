class Solution:
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        result = []

        def dfs(node, is_root):
            if not node:
                return None
            
            deleted = node.val in to_delete_set
            
            if is_root and not deleted:
                result.append(node)
            
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)
            
            return None if deleted else node

        dfs(root, True)
        return result
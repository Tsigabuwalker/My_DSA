class Solution:
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path):
            if not node:
                return

            # Add current node to path
            path.append(str(node.val))

            # If it's a leaf, save the path
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            # Backtrack
            path.pop()

        dfs(root, [])
        return result

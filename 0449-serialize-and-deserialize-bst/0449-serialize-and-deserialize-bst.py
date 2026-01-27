class Codec:
    def serialize(self, root) -> str:
        """Encodes a tree to a single string."""
        vals = []
        def pre_order(node):
            if node:
                vals.append(str(node.val))
                pre_order(node.left)
                pre_order(node.right)
        
        pre_order(root)
        return " ".join(vals)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        # Convert string to a queue of integers
        from collections import deque
        nodes = deque(int(x) for x in data.split())
        
        def build(lower, upper):
            # If the next node value doesn't fit in the current BST range,
            # it belongs to a different subtree.
            if nodes and lower < nodes[0] < upper:
                val = nodes.popleft()
                root = TreeNode(val)
                root.left = build(lower, val)
                root.right = build(val, upper)
                return root
            return None
        
        import math
        return build(-math.inf, math.inf)
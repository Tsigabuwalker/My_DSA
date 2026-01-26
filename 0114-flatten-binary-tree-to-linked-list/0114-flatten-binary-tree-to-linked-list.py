class Solution:
    def flatten(self, root):
        if not root:
            return
        
        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Store the right subtree
        temp_right = root.right
        
        # Move left subtree to right
        root.right = root.left
        root.left = None
        
        # Find the tail of the new right subtree
        curr = root
        while curr.right:
            curr = curr.right
        
        # Attach the original right subtree
        curr.right = temp_right

# Do NOT define TreeNode; just use the Solution class
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        def build(pre, post):
            if not pre:
                return None
            root = TreeNode(pre[0])  # Use LeetCode's TreeNode
            if len(pre) == 1:
                return root

            left_root_val = pre[1]
            left_size = 0
            for i in range(len(post)):
                if post[i] == left_root_val:
                    left_size = i + 1
                    break

            root.left = build(pre[1:1+left_size], post[:left_size])
            root.right = build(pre[1+left_size:], post[left_size:-1])
            return root

        return build(preorder, postorder)

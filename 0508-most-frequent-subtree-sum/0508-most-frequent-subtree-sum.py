from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
            
        counts = Counter()
        
        def get_sum(node):
            if not node:
                return 0
            
            total = node.val + get_sum(node.left) + get_sum(node.right)
            counts[total] += 1
            return total
            
        get_sum(root)
        
        max_freq = max(counts.values())
        
        return [s for s in counts if counts[s] == max_freq]
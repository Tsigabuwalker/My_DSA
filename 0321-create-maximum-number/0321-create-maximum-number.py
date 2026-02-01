class Solution:
    def maxNumber(self, nums1, nums2, k):
        
        def maxSubsequence(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]
        
        def merge(a, b):
            res = []
            while a or b:
                # pick lexicographically larger
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res
        
        best = []
        m, n = len(nums1), len(nums2)
        
        for i in range(max(0, k - n), min(k, m) + 1):
            part1 = maxSubsequence(nums1, i)
            part2 = maxSubsequence(nums2, k - i)
            candidate = merge(part1[:], part2[:])
            best = max(best, candidate)
        
        return best

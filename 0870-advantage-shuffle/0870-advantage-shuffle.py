class Solution:
    def advantageCount(self, nums1, nums2):
        n = len(nums1)
        nums1.sort()
        nums2_indexed = sorted([(val, i) for i, val in enumerate(nums2)])
        
        res = [0] * n
        left = 0
        right = n - 1
        
        for val, i in reversed(nums2_indexed):
            if nums1[right] > val:
                res[i] = nums1[right]
                right -= 1
            else:
                res[i] = nums1[left]
                left += 1
        
        return res

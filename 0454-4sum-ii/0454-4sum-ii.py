class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        sum_map = {}
        count = 0
        
        # Step 1: Store all sums of nums1 and nums2 in a hash map
        for a in nums1:
            for b in nums2:
                s = a + b
                sum_map[s] = sum_map.get(s, 0) + 1
        
        # Step 2: For each sum of nums3 and nums4, check for the complement
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_map:
                    count += sum_map[target]
                    
        return count
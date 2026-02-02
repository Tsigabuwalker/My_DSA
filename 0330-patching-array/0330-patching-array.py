class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        miss = 1
        patches = 0
        i = 0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                # We can form the next range using the existing number
                miss += nums[i]
                i += 1
            else:
                # We have a gap, so we patch by adding 'miss'
                miss += miss
                patches += 1
                
        return patches
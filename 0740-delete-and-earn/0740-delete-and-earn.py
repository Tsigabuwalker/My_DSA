class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num
        
        take, skip = 0, 0
        for i in range(len(points)):
            take_i = skip + points[i]
            skip_i = max(skip, take)
            take, skip = take_i, skip_i
        
        return max(take, skip)
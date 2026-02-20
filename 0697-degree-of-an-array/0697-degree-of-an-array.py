class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        last = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num not in count:
                count[num] = 0
                first[num] = i
            
            count[num] += 1
            last[num] = i
        
        degree = 0
        for num in count:
            if count[num] > degree:
                degree = count[num]
        
        min_length = len(nums)
        
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                if length < min_length:
                    min_length = length
        
        return min_length
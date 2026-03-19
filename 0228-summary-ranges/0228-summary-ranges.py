class Solution:
    def summaryRanges(self, nums):
        result = []
        
        if not nums:
            return result
        
        start = nums[0]  # beginning of range
        
        for i in range(1, len(nums)):
            # if not consecutive
            if nums[i] != nums[i - 1] + 1:
                # close the current range
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                
                # start new range
                start = nums[i]
        
        # add the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result
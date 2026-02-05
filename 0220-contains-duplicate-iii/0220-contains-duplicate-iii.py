class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        buckets = {}
        width = valueDiff + 1
        
        for i in range(len(nums)):
            bucket_id = nums[i] // width
            
            if bucket_id in buckets:
                return True
            
            if (bucket_id - 1) in buckets and abs(nums[i] - buckets[bucket_id - 1]) < width:
                return True
            
            if (bucket_id + 1) in buckets and abs(nums[i] - buckets[bucket_id + 1]) < width:
                return True
            
            buckets[bucket_id] = nums[i]
            
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // width]
                
        return False
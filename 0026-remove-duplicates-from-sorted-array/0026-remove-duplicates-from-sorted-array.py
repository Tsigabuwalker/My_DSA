class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # 'insert_pos' starts at 1 because the first element is always unique
        insert_pos = 1
        
        # Iterate from the second element to the end
        for curr in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[curr] != nums[curr - 1]:
                nums[insert_pos] = nums[curr]
                insert_pos += 1
        
        # insert_pos now represents the count of unique elements (k)
        return insert_pos
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k tracks the position for the next non-val element
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                # Place the valid element at index k
                nums[k] = nums[i]
                # Increment k to the next available slot
                k += 1
                
        return k
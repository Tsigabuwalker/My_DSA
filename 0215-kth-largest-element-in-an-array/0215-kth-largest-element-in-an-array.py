class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k
        
        def partition(left, right):
            pivot = nums[right]
            fill_ptr = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[fill_ptr], nums[i] = nums[i], nums[fill_ptr]
                    fill_ptr += 1
            nums[fill_ptr], nums[right] = nums[right], nums[fill_ptr]
            return fill_ptr

        def select(left, right):
            pivot_idx = partition(left, right)
            
            if pivot_idx == target:
                return nums[pivot_idx]
            elif pivot_idx < target:
                return select(pivot_idx + 1, right)
            else:
                return select(left, pivot_idx - 1)

        return select(0, len(nums) - 1)
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        def sort_array(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return sort_array(left) + middle + sort_array(right)

        sorted_nums = sort_array(nums)
        median = sorted_nums[len(nums) // 2]
        
        moves = 0
        for n in nums:
            moves += abs(n - median)
            
        return moves
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater_map = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                next_greater_map[smaller_num] = num
            stack.append(num)
            
        return [next_greater_map.get(num, -1) for num in nums1]
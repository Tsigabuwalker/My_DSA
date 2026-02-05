class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        def sort_array(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return sort_array(left) + middle + sort_array(right)

        g = sort_array(g)
        s = sort_array(s)
        
        child_i = 0
        cookie_j = 0
        
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
                
        return child_i
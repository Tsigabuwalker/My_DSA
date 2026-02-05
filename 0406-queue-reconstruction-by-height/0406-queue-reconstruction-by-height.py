class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            
            left = [x for x in arr if x[0] > pivot[0] or (x[0] == pivot[0] and x[1] < pivot[1])]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x[0] < pivot[0] or (x[0] == pivot[0] and x[1] > pivot[1])]
            
            return quicksort(left) + middle + quicksort(right)

        sorted_people = quicksort(people)
        
        res = []
        for p in sorted_people:
            res.insert(p[1], p)
            
        return res
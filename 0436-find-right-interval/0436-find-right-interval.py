class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        starts = []
        for i in range(n):
            starts.append([intervals[i][0], i])
        
        starts.sort()
        
        res = []
        for i in range(n):
            target = intervals[i][1]
            
            low = 0
            high = n
            found_idx = -1
            
            while low < high:
                mid = (low + high) // 2
                if starts[mid][0] >= target:
                    found_idx = starts[mid][1]
                    high = mid
                else:
                    low = mid + 1
            
            res.append(found_idx)
            
        return res
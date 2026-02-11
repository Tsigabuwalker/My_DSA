class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        res = 0
        p1, p2 = -1, -1
        
        for s, e in intervals:
            if s <= p1:
                continue
            
            if s <= p2:
                res += 1
                p1 = p2
                p2 = e
            else:
                res += 2
                p1 = e - 1
                p2 = e
                
        return res
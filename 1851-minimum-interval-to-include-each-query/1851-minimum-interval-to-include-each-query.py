import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        queries_with_index = sorted((q, i) for i, q in enumerate(queries))
        
        res = [-1] * len(queries)
        heap = []
        i = 0  # pointer for intervals
        
        for q, idx in queries_with_index:
            # Add all intervals starting before q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                size = r - l + 1
                heapq.heappush(heap, (size, r))
                i += 1
            
            # Remove intervals that end before q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            # Top of heap is smallest interval covering q
            if heap:
                res[idx] = heap[0][0]
            else:
                res[idx] = -1
        
        return res

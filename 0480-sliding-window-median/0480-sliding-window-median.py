import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small = [] # Max-heap (invert values)
        large = [] # Min-heap
        delayed = defaultdict(int)
        res = []
        
        def balance():
            while small and delayed[-small[0]] > 0:
                delayed[-heapq.heappop(small)] -= 1
            while large and delayed[large[0]] > 0:
                delayed[heapq.heappop(large)] -= 1

        small_size, large_size = 0, 0
        
        for i in range(k):
            heapq.heappush(small, -nums[i])
            small_size += 1
        
        for _ in range(k // 2):
            heapq.heappush(large, -heapq.heappop(small))
            small_size -= 1
            large_size += 1
            
        balance()
        res.append(-small[0] if k % 2 == 1 else (-small[0] + large[0]) / 2.0)
        
        for i in range(k, len(nums)):
            out_num = nums[i - k]
            in_num = nums[i]
            balance_diff = -1 if out_num <= -small[0] else 1
            delayed[out_num] += 1
            
            if small and in_num <= -small[0]:
                heapq.heappush(small, -in_num)
                balance_diff += 1
            else:
                heapq.heappush(large, in_num)
                balance_diff -= 1
            
            if balance_diff < 0:
                heapq.heappush(small, -heapq.heappop(large))
            elif balance_diff > 0:
                heapq.heappush(large, -heapq.heappop(small))
                
            balance()
            res.append(-small[0] if k % 2 == 1 else (-small[0] + large[0]) / 2.0)
            
        return res
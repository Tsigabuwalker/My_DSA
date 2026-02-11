import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = []
        
        # Create (ratio, quality) pairs
        for q, w in zip(quality, wage):
            workers.append((w / q, q))
        
        # Sort by ratio ascending
        workers.sort()
        
        heap = []
        total_quality = 0
        min_cost = float('inf')
        
        for ratio, q in workers:
            heapq.heappush(heap, -q)  # max heap using negative
            total_quality += q
            
            # If more than k workers, remove largest quality
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
            
            # If exactly k workers, compute cost
            if len(heap) == k:
                cost = total_quality * ratio
                min_cost = min(min_cost, cost)
        
        return min_cost

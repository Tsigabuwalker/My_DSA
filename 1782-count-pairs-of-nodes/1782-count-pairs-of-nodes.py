class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        from collections import defaultdict
        
        degree = [0] * (n + 1)
        count = defaultdict(int)
        
        # Step 1: count degrees and shared edges
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            if u > v:
                u, v = v, u
            count[(u, v)] += 1
        
        sorted_degree = sorted(degree[1:])
        res = []
        
        # Step 2: process each query
        for q in queries:
            total = 0
            left, right = 0, n - 1
            
            # Two pointer count
            while left < right:
                if sorted_degree[left] + sorted_degree[right] > q:
                    total += (right - left)
                    right -= 1
                else:
                    left += 1
            
            # Step 3: subtract invalid pairs
            for (u, v), shared in count.items():
                if degree[u] + degree[v] > q and degree[u] + degree[v] - shared <= q:
                    total -= 1
            
            res.append(total)
        
        return res

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = [[] for _ in range(n)]
        
        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))
        
        dist = [float('inf')] * n
        dist[0] = 0
        
        heap = [(0, 0)]  # (distance, node)
        
        while heap:
            heap.sort()
            d, node = heap.pop(0)
            
            if d > dist[node]:
                continue
            
            for nei, weight in graph[node]:
                newDist = d + weight
                if newDist < dist[nei]:
                    dist[nei] = newDist
                    heap.append((newDist, nei))
        
        result = 0
        
        # Count original nodes
        for d in dist:
            if d <= maxMoves:
                result += 1
        
        # Count subdivided nodes
        for u, v, cnt in edges:
            from_u = max(0, maxMoves - dist[u])
            from_v = max(0, maxMoves - dist[v])
            result += min(cnt, from_u + from_v)
        
        return result
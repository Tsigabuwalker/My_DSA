class Solution:
    def findItinerary(self, tickets: list[list[int]]) -> list[str]:
        adj = {}
        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)
        
        for src in adj:
            adj[src].sort(reverse=True)
            
        stack = ["JFK"]
        res = []
        
        while stack:
            curr = stack[-1]
            if curr in adj and adj[curr]:
                stack.append(adj[curr].pop())
            else:
                res.append(stack.pop())
                
        return res[::-1]
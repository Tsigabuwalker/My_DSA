from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Build graph and indegree array
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        # Initialize queue with nodes having indegree 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If order contains all courses, return it; else return []
        return order if len(order) == numCourses else []

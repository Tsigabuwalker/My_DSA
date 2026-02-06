class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        
        # Precompute positions of each character in the ring
        pos = {}
        for i, c in enumerate(ring):
            if c not in pos:
                pos[c] = []
            pos[c].append(i)
        
        # Memoization dictionary
        self.memo = {}  # (ring_index, key_index) -> min steps

        def dfs(ring_index, key_index):
            if key_index == len(key):
                return 0
            if (ring_index, key_index) in self.memo:
                return self.memo[(ring_index, key_index)]
            
            min_steps = float('inf')
            target_char = key[key_index]
            
            # Try moving to every occurrence of the target character
            for next_index in pos[target_char]:
                # Circular distance
                step = min(abs(ring_index - next_index), n - abs(ring_index - next_index))
                # 1 step for pressing the button
                total = step + 1 + dfs(next_index, key_index + 1)
                if total < min_steps:
                    min_steps = total
            
            self.memo[(ring_index, key_index)] = min_steps
            return min_steps
        
        # Start from position 0, first character of key
        return dfs(0, 0)


# Example usage
solution = Solution()
print(solution.findRotateSteps("godding", "gd"))       # Output: 4
print(solution.findRotateSteps("godding", "godding"))  # Output: 13

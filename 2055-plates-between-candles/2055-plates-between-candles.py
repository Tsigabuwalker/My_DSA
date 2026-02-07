class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        prefix = [0] * n
        left_candle = [-1] * n
        right_candle = [-1] * n
        
        # Step 1: prefix sum of plates
        plates = 0
        for i in range(n):
            if s[i] == '*':
                plates += 1
            prefix[i] = plates
        
        # Step 2: nearest candle to the left
        nearest = -1
        for i in range(n):
            if s[i] == '|':
                nearest = i
            left_candle[i] = nearest
        
        # Step 3: nearest candle to the right
        nearest = -1
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                nearest = i
            right_candle[i] = nearest
        
        # Step 4: answer queries
        res = []
        for l, r in queries:
            first = right_candle[l]   # first candle in range
            last = left_candle[r]     # last candle in range
            if first != -1 and last != -1 and first < last:
                res.append(prefix[last] - prefix[first])
            else:
                res.append(0)
        
        return res

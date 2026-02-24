class Solution:
    def shortestSuperstring(self, words):
        n = len(words)
        
        # 1️⃣ Compute overlap cost (how many extra chars we need to add)
        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    w1, w2 = words[i], words[j]
                    max_overlap = min(len(w1), len(w2))
                    for k in range(max_overlap, -1, -1):
                        if w1.endswith(w2[:k]):
                            overlap[i][j] = len(w2) - k
                            break
        
        # 2️⃣ dp[mask][i] = minimum length superstring
        # that uses words in mask and ends at word i
        dp = [[float('inf')]*n for _ in range(1<<n)]
        parent = [[-1]*n for _ in range(1<<n)]
        
        # Base case
        for i in range(n):
            dp[1<<i][i] = len(words[i])
        
        # 3️⃣ Fill DP
        for mask in range(1<<n):
            for last in range(n):
                if not (mask & (1<<last)):
                    continue
                prev_mask = mask ^ (1<<last)
                if prev_mask == 0:
                    continue
                
                for prev in range(n):
                    if prev_mask & (1<<prev):
                        cand = dp[prev_mask][prev] + overlap[prev][last]
                        if cand < dp[mask][last]:
                            dp[mask][last] = cand
                            parent[mask][last] = prev
        
        # 4️⃣ Find best ending word
        full_mask = (1<<n) - 1
        last = min(range(n), key=lambda i: dp[full_mask][i])
        
        # 5️⃣ Reconstruct path
        path = []
        mask = full_mask
        while last != -1:
            path.append(last)
            temp = parent[mask][last]
            mask ^= (1<<last)
            last = temp
        
        path.reverse()
        
        # 6️⃣ Build result string
        res = words[path[0]]
        for i in range(1, len(path)):
            prev = path[i-1]
            curr = path[i]
            add_len = overlap[prev][curr]
            res += words[curr][-add_len:] if add_len else words[curr]
        
        return res
class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        bad = {}
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                bad[fronts[i]] = True
        
        ans = 2001  # since max value is 2000
        for x in fronts + backs:
            if x not in bad:
                ans = min(ans, x)
        
        if ans == 2001:
            return 0
        return ans

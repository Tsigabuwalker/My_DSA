from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2 = sorted(set(arr2))  # sort + remove duplicates
        
        dp = {-1: 0}  # {last_value: operations}
        
        for num in arr1:
            new_dp = {}
            
            for prev, ops in dp.items():
                # Option 1: keep num
                if num > prev:
                    if num not in new_dp or new_dp[num] > ops:
                        new_dp[num] = ops
                
                # Option 2: replace with next greater in arr2
                idx = bisect_right(arr2, prev)
                if idx < len(arr2):
                    replace = arr2[idx]
                    if replace not in new_dp or new_dp[replace] > ops + 1:
                        new_dp[replace] = ops + 1
            
            dp = new_dp
            
            if not dp:
                return -1
        
        return min(dp.values())
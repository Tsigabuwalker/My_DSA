class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        low, high = 0, 1.0
        
        while low < high:
            mid = (low + high) / 2
            count = 0
            max_frac = [0, 1]
            j = 1
            
            for i in range(n - 1):
                while j < n and arr[i] > mid * arr[j]:
                    j += 1
                
                count += (n - j)
                
                if j < n and arr[i] / arr[j] > max_frac[0] / max_frac[1]:
                    max_frac = [arr[i], arr[j]]
            
            if count == k:
                return max_frac
            elif count < k:
                low = mid
            else:
                high = mid
class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        tails = []
        
        for _, h in envelopes:
            idx = self._binary_search(tails, h)
            
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
                
        return len(tails)

    def _binary_search(self, arr, target):
        low = 0
        high = len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
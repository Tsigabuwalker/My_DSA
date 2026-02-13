class Solution:
    def maxChunksToSorted(self, arr):
        chunks = 0
        max_left = -1
        
        for i in range(len(arr)):
            max_left = max(max_left, arr[i])
            
            if max_left == i:
                chunks += 1
        
        return chunks

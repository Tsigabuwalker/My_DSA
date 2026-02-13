class Solution:
    def maxChunksToSorted(self, arr):
        sorted_arr = arr[:]
        sorted_arr.sort()
        
        count = {}
        chunks = 0
        
        for i in range(len(arr)):
            # Add current element from original array
            if arr[i] in count:
                count[arr[i]] += 1
            else:
                count[arr[i]] = 1
            
            if count[arr[i]] == 0:
                del count[arr[i]]
            
            # Subtract current element from sorted array
            if sorted_arr[i] in count:
                count[sorted_arr[i]] -= 1
            else:
                count[sorted_arr[i]] = -1
            
            if count[sorted_arr[i]] == 0:
                del count[sorted_arr[i]]
            
            # If counts match completely
            if len(count) == 0:
                chunks += 1
        
        return chunks

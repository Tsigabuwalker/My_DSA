class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        score_with_index = []
        for i in range(n):
            score_with_index.append((score[i], i))
        
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x[0] > pivot[0]]
            middle = [x for x in arr if x[0] == pivot[0]]
            right = [x for x in arr if x[0] < pivot[0]]
            return quicksort(left) + middle + quicksort(right)
            
        sorted_scores = quicksort(score_with_index)
        
        res = ["" for _ in range(n)]
        
        for i in range(n):
            original_idx = sorted_scores[i][1]
            if i == 0:
                res[original_idx] = "Gold Medal"
            elif i == 1:
                res[original_idx] = "Silver Medal"
            elif i == 2:
                res[original_idx] = "Bronze Medal"
            else:
                res[original_idx] = str(i + 1)
                
        return res
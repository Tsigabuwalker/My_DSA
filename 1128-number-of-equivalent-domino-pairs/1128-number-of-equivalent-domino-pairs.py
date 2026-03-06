class Solution:
    def numEquivDominoPairs(self, dominoes):
        # Dictionary implemented manually using Python dict
        freq = {}
        result = 0
        
        for d in dominoes:
            a, b = d[0], d[1]
            # Normalize: always store as (min, max)
            if a < b:
                key = (a, b)
            else:
                key = (b, a)
            
            # Count pairs on the fly
            if key in freq:
                result += freq[key]   # each new domino forms 'freq[key]' new pairs
                freq[key] += 1
            else:
                freq[key] = 1
        
        return result


# Example 1
dominoes1 = [[1,2],[2,1],[3,4],[5,6]]
print(Solution().numEquivDominoPairs(dominoes1))  # Output: 1

# Example 2
dominoes2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(Solution().numEquivDominoPairs(dominoes2))  # Output: 3

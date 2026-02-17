class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            # compare remaining substrings
            if word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        
        # append the remaining characters
        merge.append(word1[i:])
        merge.append(word2[j:])
        
        return ''.join(merge)

class Solution:
    def commonChars(self, words):
        freq = [float('inf')] * 26
        
        for word in words:
            temp = [0] * 26
            
            for ch in word:
                temp[ord(ch) - ord('a')] += 1
            
            for i in range(26):
                if temp[i] < freq[i]:
                    freq[i] = temp[i]
        
        result = []
        
        for i in range(26):
            while freq[i] > 0:
                result.append(chr(i + ord('a')))
                freq[i] -= 1
        
        return result
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        count = [0] * 26
        k = 0
        
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                k += 1
            else:
                k = 1
            index = ord(s[i]) - ord('a')
            count[index] = max(count[index], k)
        
        return sum(count)

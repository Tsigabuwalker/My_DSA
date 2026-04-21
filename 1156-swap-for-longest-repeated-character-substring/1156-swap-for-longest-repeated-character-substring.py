class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import Counter
        
        count = Counter(text)
        result = 0
        
        for ch in count:
            left = 0
            mismatch = 0
            
            for right in range(len(text)):
                if text[right] != ch:
                    mismatch += 1
                
                while mismatch > 1:
                    if text[left] != ch:
                        mismatch -= 1
                    left += 1
                
                # window length
                window = right - left + 1
                
                # cannot exceed total occurrences of ch
                result = max(result, min(window, count[ch]))
        
        return result
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        
        freq = Counter(s)
        stack = []
        seen = set()
        
        for ch in s:
            freq[ch] -= 1
            
            if ch in seen:
                continue
            
            while stack and ch < stack[-1] and freq[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            
            stack.append(ch)
            seen.add(ch)
        
        return "".join(stack)

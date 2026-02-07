class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Helper function to find max consecutive of char 'ch' with at most k flips
        def maxConsecutiveChar(ch: str) -> int:
            left = 0
            flips = 0
            max_len = 0
            
            for right in range(len(answerKey)):
                if answerKey[right] != ch:
                    flips += 1
                
                # If flips exceed k, shrink window from left
                while flips > k:
                    if answerKey[left] != ch:
                        flips -= 1
                    left += 1
                
                max_len = max(max_len, right - left + 1)
            
            return max_len
        
        # Maximum consecutive either 'T' or 'F'
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))

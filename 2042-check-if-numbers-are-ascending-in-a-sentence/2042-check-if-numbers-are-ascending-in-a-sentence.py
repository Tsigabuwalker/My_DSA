class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        prev_num = -1
        
        for token in tokens:
            if token.isdigit():  # token is a number
                num = int(token)
                if num <= prev_num:  # not strictly increasing
                    return False
                prev_num = num
        
        return True

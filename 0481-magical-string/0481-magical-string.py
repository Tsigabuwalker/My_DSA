class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1  # first three numbers are 1,2,2 → only 1 one
        
        s = [1, 2, 2]
        i = 2  # pointer to read count
        num = 1  # next number to append
        
        while len(s) < n:
            count = s[i]
            s.extend([num] * count)
            num = 3 - num  # flip between 1 and 2
            i += 1
        
        return s[:n].count(1)

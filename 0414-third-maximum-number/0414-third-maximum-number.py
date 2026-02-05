class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        m1 = m2 = m3 = -float('inf')
        
        for n in nums:
            if n == m1 or n == m2 or n == m3:
                continue
                
            if n > m1:
                m1, m2, m3 = n, m1, m2
            elif n > m2:
                m2, m3 = n, m2
            elif n > m3:
                m3 = n
        
        return m3 if m3 != -float('inf') else m1
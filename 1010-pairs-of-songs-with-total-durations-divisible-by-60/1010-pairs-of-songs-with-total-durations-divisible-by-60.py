class Solution:
    def numPairsDivisibleBy60(self, time):
        count = [0] * 60
        result = 0
        
        for t in time:
            r = t % 60
            complement = (60 - r) % 60
            
            result += count[complement]
            count[r] += 1
        
        return result
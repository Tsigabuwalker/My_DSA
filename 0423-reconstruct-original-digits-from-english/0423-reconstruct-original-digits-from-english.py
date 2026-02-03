from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count all letters in the input string
        counts = Counter(s)
        
        # Array to store the count of each digit 0-9
        res = [0] * 10
        
        # Round 1: Unique characters
        res[0] = counts['z']
        res[2] = counts['w']
        res[4] = counts['u']
        res[6] = counts['x']
        res[8] = counts['g']
        
        # Round 2: Derived counts
        # 'three' has 'h', but so does 'eight'
        res[3] = counts['h'] - res[8]
        # 'five' has 'f', but so does 'four'
        res[5] = counts['f'] - res[4]
        # 'seven' has 's', but so does 'six'
        res[7] = counts['s'] - res[6]
        # 'one' has 'o', but so do 'zero', 'two', 'four'
        res[1] = counts['o'] - res[0] - res[2] - res[4]
        # 'nine' has 'i', but so do 'five', 'six', 'eight'
        res[9] = counts['i'] - res[5] - res[6] - res[8]
        
        # Build the final string in ascending order
        output = []
        for i in range(10):
            output.append(str(i) * res[i])
            
        return "".join(output)
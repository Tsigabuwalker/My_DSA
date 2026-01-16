class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current_str = "1"
        
        # We already have n=1, so we repeat the process n-1 times
        for _ in range(n - 1):
            next_str = []
            i = 0
            
            # Process current_str to find the next_str
            while i < len(current_str):
                count = 1
                # Move pointer i while characters are the same
                while i + 1 < len(current_str) and current_str[i] == current_str[i + 1]:
                    i += 1
                    count += 1
                
                # Append the count followed by the digit character
                next_str.append(str(count))
                next_str.append(current_str[i])
                
                # Move to the next unique character
                i += 1
            
            # Join list into string for the next iteration
            current_str = "".join(next_str)
            
        return current_str
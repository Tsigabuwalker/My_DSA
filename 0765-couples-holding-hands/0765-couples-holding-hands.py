class Solution:
    def minSwapsCouples(self, row):
        n = len(row)
        
        # Store position of each person
        position = {}
        for i in range(n):
            position[row[i]] = i
        
        swaps = 0
        
        for i in range(0, n, 2):
            first = row[i]
            partner = first ^ 1
            
            if row[i + 1] != partner:
                swaps += 1
                
                partner_index = position[partner]
                
                # Swap
                row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
                
                # Update positions
                position[row[partner_index]] = partner_index
                position[row[i + 1]] = i + 1
        
        return swaps

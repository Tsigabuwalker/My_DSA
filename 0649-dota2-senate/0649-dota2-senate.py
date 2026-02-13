class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate)
        
        radiant = []
        dire = []
        
        # Store indices
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # Simulate rounds
        while len(radiant) > 0 and len(dire) > 0:
            r_index = radiant.pop(0)
            d_index = dire.pop(0)
            
            if r_index < d_index:
                # Radiant bans Dire
                radiant.append(r_index + n)
            else:
                # Dire bans Radiant
                dire.append(d_index + n)
        
        if len(radiant) > 0:
            return "Radiant"
        else:
            return "Dire"

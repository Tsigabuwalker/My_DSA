class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        # Locations are between 0 and 1000
        changes = [0] * 1001
        
        # Apply difference array logic
        for numPassengers, start, end in trips:
            changes[start] += numPassengers
            changes[end] -= numPassengers
        
        current_passengers = 0
        
        # Sweep through all locations
        for i in range(1001):
            current_passengers += changes[i]
            if current_passengers > capacity:
                return False
        
        return True

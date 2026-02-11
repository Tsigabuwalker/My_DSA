class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair position and speed
        cars = list(zip(position, speed))
        
        # Sort by position descending (closest to target first)
        cars.sort(reverse=True)
        
        fleets = 0
        last_time = 0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            # If this car takes longer, it forms a new fleet
            if time > last_time:
                fleets += 1
                last_time = time
        
        return fleets

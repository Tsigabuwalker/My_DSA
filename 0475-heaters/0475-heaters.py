class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        def sort_array(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return sort_array(left) + middle + sort_array(right)

        heaters = sort_array(heaters)
        max_radius = 0
        n = len(heaters)
        
        for house in houses:
            low = 0
            high = n
            while low < high:
                mid = (low + high) // 2
                if heaters[mid] < house:
                    low = mid + 1
                else:
                    high = mid
            
            dist_right = heaters[low] - house if low < n else float('inf')
            dist_left = house - heaters[low - 1] if low > 0 else float('inf')
            
            current_min_dist = dist_right if dist_right < dist_left else dist_left
            if current_min_dist > max_radius:
                max_radius = current_min_dist
                
        return max_radius
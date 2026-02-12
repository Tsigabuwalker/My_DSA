class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        result = set()
        i = 0
        xi = 1
        
        while xi <= bound:
            j = 0
            yj = 1
            while xi + yj <= bound:
                result.add(xi + yj)
                if y == 1:
                    break
                yj *= y
                j += 1
            if x == 1:
                break
            xi *= x
            i += 1
        
        return list(result)

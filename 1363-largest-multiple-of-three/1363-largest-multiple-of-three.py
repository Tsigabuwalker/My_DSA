class Solution:
    def largestMultipleOfThree(self, digits):
        digits.sort()
        total = sum(digits)
        remainder = total % 3
        
        # Helper to remove digits
        def remove_digits(rem, count):
            removed = 0
            for i in range(len(digits)):
                if digits[i] % 3 == rem and digits[i] != -1:
                    digits[i] = -1
                    removed += 1
                    if removed == count:
                        return True
            return False
        
        if remainder == 1:
            if not remove_digits(1, 1):
                remove_digits(2, 2)
        elif remainder == 2:
            if not remove_digits(2, 1):
                remove_digits(1, 2)
        
        # Keep valid digits
        result = [d for d in digits if d != -1]
        
        if not result:
            return ""
        
        result.sort(reverse=True)
        
        # Handle leading zeros
        if result[0] == 0:
            return "0"
        
        return "".join(map(str, result))

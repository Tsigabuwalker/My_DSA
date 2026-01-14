class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the mapping in descending order
        mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_parts = []
        
        for value, symbol in mapping:
            # If the number is zero, we are done
            if num == 0: 
                break
                
            # Determine how many times this symbol fits
            count, num = divmod(num, value)
            
            # Append the symbol 'count' times
            roman_parts.append(symbol * count)
            
        return "".join(roman_parts)
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        num &= 0xFFFFFFFF  # handle negative numbers with 32-bit two's complement
        result = ""
        
        while num > 0:
            result = hex_chars[num & 0xF] + result
            num >>= 4
        
        return result

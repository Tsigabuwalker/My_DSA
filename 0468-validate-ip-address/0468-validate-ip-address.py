class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def isIPv4(s):
            parts = s.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if not 0 <= int(part) <= 255:
                    return False
                if part != "0" and part[0] == "0":  # leading zero check
                    return False
            return True

        def isIPv6(s):
            parts = s.split(":")
            if len(parts) != 8:
                return False
            hex_digits = "0123456789abcdefABCDEF"
            for part in parts:
                if not 1 <= len(part) <= 4:
                    return False
                for ch in part:
                    if ch not in hex_digits:
                        return False
            return True

        if queryIP.count(".") == 3 and isIPv4(queryIP):
            return "IPv4"
        elif queryIP.count(":") == 7 and isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"

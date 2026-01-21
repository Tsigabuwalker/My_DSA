class Solution:
    def restoreIpAddresses(self, s: str):
        result = []

        def backtrack(start, path):
            # If we have 4 parts and used all digits, it's valid
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            # Try 1 to 3 digit segments
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start+length]

                # Check if segment is valid
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue

                backtrack(start + length, path + [segment])

        backtrack(0, [])
        return result

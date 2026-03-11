class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        subs = []

        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1

            # found a special substring
            if count == 0:
                # recursively process inside
                inner = self.makeLargestSpecial(s[start+1:i])
                subs.append("1" + inner + "0")
                start = i + 1

        # sort descending for lexicographically largest
        subs.sort(reverse=True)

        return "".join(subs)
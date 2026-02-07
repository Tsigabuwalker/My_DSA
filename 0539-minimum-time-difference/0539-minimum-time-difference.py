class Solution:
    def findMinDifference(self, timePoints):
        minutes = []
        seen = {}

        for t in timePoints:
            h = (ord(t[0]) - 48) * 10 + (ord(t[1]) - 48)
            m = (ord(t[3]) - 48) * 10 + (ord(t[4]) - 48)
            total = h * 60 + m

            if total in seen:
                return 0

            seen[total] = True
            minutes.append(total)

        minutes.sort()

        ans = 1440
        n = len(minutes)

        for i in range(1, n):
            diff = minutes[i] - minutes[i - 1]
            if diff < ans:
                ans = diff

        wrap = 1440 - minutes[-1] + minutes[0]
        if wrap < ans:
            ans = wrap

        return ans

class Solution:
    def minStickers(self, stickers, target):
        sticker_counts = []
        for sticker in stickers:
            count = [0] * 26
            for ch in sticker:
                count[ord(ch) - ord('a')] += 1
            sticker_counts.append(count)

        memo = {}
        memo[""] = 0

        def dfs(remain):
            if remain in memo:
                return memo[remain]

            remain_count = [0] * 26
            for ch in remain:
                remain_count[ord(ch) - ord('a')] += 1

            res = float('inf')

            for sticker in sticker_counts:
                if sticker[ord(remain[0]) - ord('a')] == 0:
                    continue

                new_remain = ""
                for i in range(26):
                    if remain_count[i] > 0:
                        needed = remain_count[i] - sticker[i]
                        if needed > 0:
                            new_remain += chr(i + ord('a')) * needed

                temp = dfs(new_remain)
                if temp != -1:
                    if 1 + temp < res:
                        res = 1 + temp

            if res == float('inf'):
                memo[remain] = -1
            else:
                memo[remain] = res

            return memo[remain]

        return dfs(target)
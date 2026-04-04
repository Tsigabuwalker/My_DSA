class Solution:
    def beautifulArray(self, n):
        res = [1]
        while len(res) < n:
            temp = []
            for x in res:
                if 2*x - 1 <= n:
                    temp.append(2*x - 1)
            for x in res:
                if 2*x <= n:
                    temp.append(2*x)
            res = temp
        return res


sol = Solution()
print(sol.beautifulArray(4))  # Example output: [2,1,4,3]
print(sol.beautifulArray(5))  # Example output: [3,1,2,5,4]

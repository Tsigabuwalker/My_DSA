from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = list(map(str, nums))

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1   # a should come first
            elif a + b < b + a:
                return 1    # b should come first
            else:
                return 0

        nums.sort(key=cmp_to_key(compare))

        result = ''.join(nums)

        # Handle case like "000"
        return '0' if result[0] == '0' else result

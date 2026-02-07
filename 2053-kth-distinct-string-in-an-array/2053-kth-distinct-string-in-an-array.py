class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        # Step 1: Count occurrences manually
        count = {}
        for string in arr:
            if string in count:
                count[string] += 1
            else:
                count[string] = 1

        # Step 2: Find the kth distinct string
        for string in arr:
            if count[string] == 1:
                k -= 1
                if k == 0:
                    return string

        # If fewer than k distinct strings
        return ""

class Solution:
    def canReorderDoubled(self, arr):
        # Step 1: Count occurrences
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1

        # Step 2: Sort by absolute value
        for x in sorted(count, key=abs):
            if count[x] > count.get(2 * x, 0):
                return False
            # Safely subtract only if 2*x exists
            count[2 * x] = count.get(2 * x, 0) - count[x]
            count[x] = 0  # Mark x as used

        return True

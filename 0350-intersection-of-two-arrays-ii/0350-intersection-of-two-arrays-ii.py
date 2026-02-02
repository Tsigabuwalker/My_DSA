class Solution:
    def intersect(self, nums1, nums2):
        # Count frequency of nums1 using a dict
        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        result = []

        # Check nums2 against counts
        for num in nums2:
            if counts.get(num, 0) > 0:
                result.append(num)
                counts[num] -= 1

        return result

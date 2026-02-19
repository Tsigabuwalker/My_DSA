class Solution:
    def minSwaps(self, nums, forbidden):
        n = len(nums)
        
        count_nums = {}
        count_forbidden = {}
        
        for x in nums:
            count_nums[x] = count_nums.get(x, 0) + 1
        
        for x in forbidden:
            count_forbidden[x] = count_forbidden.get(x, 0) + 1
        
        for v in count_nums:
            allowed_positions = n - count_forbidden.get(v, 0)
            if count_nums[v] > allowed_positions:
                return -1
        
        bad_count = {}
        total_bad = 0
        
        for i in range(n):
            if nums[i] == forbidden[i]:
                v = nums[i]
                bad_count[v] = bad_count.get(v, 0) + 1
                total_bad += 1
        
        if total_bad == 0:
            return 0
        
        max_bad_value = 0
        for v in bad_count:
            if bad_count[v] > max_bad_value:
                max_bad_value = bad_count[v]
        
        return max(max_bad_value, (total_bad + 1) // 2)

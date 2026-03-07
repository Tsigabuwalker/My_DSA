class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        answer = []
        left, right = 1, n
        
        # Create k distinct differences by zig-zagging
        while left <= right:
            if k > 1:
                if k % 2 == 1:
                    answer.append(left)
                    left += 1
                else:
                    answer.append(right)
                    right -= 1
                k -= 1
            else:
                # Once k distinct differences are achieved, fill in increasing order
                answer.append(left)
                left += 1
        
        return answer

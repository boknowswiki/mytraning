# dp and greedy

# time O(n)
# space O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        # The starting range of the first jump is [0, 0]
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0
        
        for i in range(n - 1):
            # Update the farthest reachable index of this jump.
            cur_far = max(cur_far, i + nums[i])

            # If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == cur_end:
                answer += 1
                cur_end = cur_far
                
        return answer

# Time Limit Exceeded
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [sys.maxsize]*n
        dp[0] = 0
        for i in range(n):
            for j in range(i+1):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n-1]

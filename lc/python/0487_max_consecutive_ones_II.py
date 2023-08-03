# array, sliding window
# time O(n)
# space O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        ret = 0
        l = 0
        zero_cnt = 0

        for r in range(n):
            if nums[r] == 0:
                zero_cnt += 1
            
            while zero_cnt > 1:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1
            
            ret = max(ret, r-l+1)

        return ret

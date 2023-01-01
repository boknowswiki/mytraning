# two pointers, binary search
# time O(n^2)
# space O(1)

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        ret = 0

        for i in range(n-2):
            ret += self.helper(nums[i+1:], target-nums[i])

        return ret

    def helper(self, nums, target):
        ret = 0
        l = 0
        r = len(nums)-1
        while l < r:
            val = nums[l] + nums[r]
            if val < target:
                ret += r-l
                l += 1
            else:
                r -= 1

        return ret

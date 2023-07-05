# sliding window
# time O(n)
# space O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        ret = 0
        left = 0

        for right in range(len(nums)):
            zero += int(nums[right] == 0)

            while left < right and zero > 1:
                zero -= int(nums[left] == 0)
                left += 1

            ret = max(ret, right-left)

        return ret

#!/usr/bin/python -t

class Solution:
    """
    @param nums: an integer array.
    @return: return the possible longest length of the subarray that elements are the same.
    """
    def threeChances(self, nums):
        # write your code here.
        if len(nums) <= 4:
            return len(nums)

        left, right = 0, 0
        cnts = [0 for i in range(30)]

        max_cnt = 0
        ret = 0
        while right < len(nums):
            num = nums[right]
            cnts[num] += 1
            max_cnt = max(max_cnt, cnts[num])
            rep = (right-left+1) - max_cnt
            if rep > 3:
                cnts[nums[left]] -= 1
                left += 1
            else:
                ret = max(ret, right-left+1)

            right += 1
        
        return ret

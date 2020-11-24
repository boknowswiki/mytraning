#!/usr/bin/python -t

class Solution:
    """
    @param nums: an array
    @return: the shortest subarray's length
    """
    def findUnsortedSubarray(self, nums):
        # Write your code here
        sortedNums = sorted(nums)
        ans = len(nums)
        while ans > 0 and nums[ans - 1] == sortedNums[ans - 1]:
            ans -= 1
        temp = 0
        for i in range(ans):
            if nums[i] == sortedNums[i]:
                temp += 1
            else:
                break
        return ans - temp

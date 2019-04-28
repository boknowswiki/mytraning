#!/usr/bin/python -t

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ret = []
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = n - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                
                if total == 0:
                    ret.append((nums[i], nums[start], nums[end]))
                    while start < end and nums[start] == nums[start+1]:
                        start = start + 1
                    while start < end and nums[end] == nums[end-1]:
                        end = end - 1
                    start = start + 1
                    end = end - 1
                elif total < 0:
                    start = start + 1
                else:
                    end = end - 1

                
        return ret

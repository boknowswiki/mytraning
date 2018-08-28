#!/usr/bin/python -t

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ret = []
        pre = lower - 1

        for i in xrange(len(nums)+1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]
                if cur - pre > 2:
                    ret.append("%d->%d" % (pre+1, cur-1))
                elif cur - pre == 2:
                    ret.append("%d" % (pre+1))

                pre = cur

        return ret


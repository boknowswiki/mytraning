#!/usr/bin/python -t

# array
# time O(n)
# space O(1)

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        start = lower
        ranges = []

        def addRange(l, r):
            if l == r - 1:
                ranges.append(str(l))
            else:
                ranges.append("{}->{}".format(l, r-1))
        
        for n in nums:
            if start < n:
                addRange(start, n)
            start = n + 1
            
        if start <= upper:
            addRange(start, upper + 1)
        
        return ranges

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


#!/usr/bin/python -t

# binary search
# time O(nlogk)
# space O(1)

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sorted_list = SortedList()
        n = len(nums)

        for i in range(n):
            if i > indexDiff:
                sorted_list.remove(nums[i-indexDiff-1])
            pos1 = SortedList.bisect_left(sorted_list, nums[i]-valueDiff)
            pos2 = SortedList.bisect_right(sorted_list, nums[i]+valueDiff)
            if pos1 != pos2 and pos1 != len(sorted_list):
                return True

            sorted_list.add(nums[i])

        return False
        

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in xrange(n):
            m = nums[i] / w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] / w]
        return False


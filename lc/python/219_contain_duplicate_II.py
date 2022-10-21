#!/usr/bin/python -t

# two pointers and hashmap
# time O(n)
# space O(k)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        l = 0
        for r in range(len(nums)):
            if nums[r] in d:
                return True
            d[nums[r]] = r
            if r-l >= k:
                del d[nums[l]]
                l += 1
                
        return False

#Time O(n) space O(n)

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        d = {}
        
        for i in range(n):
            if nums[i] in d:
                if i - d[nums[i]] <= k:
                    return True

            d[nums[i]] = i
                
        return False

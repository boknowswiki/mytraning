#!/usr/bin/python -t

# two pointers
# time O(n)
# space O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] != val:
                if i != index:
                    nums[index] = nums[i]
                index = index + 1
        
        return index


#!/usr/bin/python -t

# two pointers and array
# time O(n)
# space O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        index = 0
        
        for i in range(1, n):
            if nums[i] != nums[index]:
                index +=1
                nums[index] = nums[i]
                
        return index+1

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        index = 0
        
        for i in range(1, n):
            if nums[index] != nums[i]:
                index = index + 1
                nums[index] = nums[i]
        return index+1


#!/usr/bin/python -t

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse_array(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j - 1
                
        n = len(nums)
        k = k % n
        
        reverse_array(nums, 0, n - 1)
        reverse_array(nums, 0, k-1)
        reverse_array(nums, k, n - 1)
        
        return


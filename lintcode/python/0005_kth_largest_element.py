#!/usr/bin/python -t

# quick select
# similar to 0461

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        l = len(nums)
        if n > l:
            return 0
            
        ret = self.quickselect(nums, 0, l-1, n-1)
        
        return ret
        
        
    def quickselect(self, nums, start, end, k):
        if start == end:
            return nums[start]
            
        part = self.partition(nums, start, end)
        
        #print nums
        
        if part == k:
            return nums[part]
        elif part < k:
            return self.quickselect(nums, part+1, end, k)
        else:
            return self.quickselect(nums, start, part-1, k)
        
        
    def partition(self, nums, start, end):
        pivot = nums[end]
        i = start
        
        while start < end:
            if nums[start] >= pivot:
                nums[i], nums[start] = nums[start], nums[i]
                i += 1
            start += 1
            
        nums[i], nums[end] = nums[end], nums[i]
        
        return i


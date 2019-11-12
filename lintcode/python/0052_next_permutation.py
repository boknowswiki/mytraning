#!/usr/bin/python -t

#1 5 2 4 3找这些数字组成的稍微大那么一点的数
#从右往左找第一个降序的地方, 把它和右边比他大的最小的换, 换完reverse回来
#1 5 3 4 2
#1 5 3 2 4


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = n-1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            
            nums[j], nums[i] = nums[i], nums[j]
            
        self.swapList(nums, i+1, n-1)

        return nums
    
        
        
    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
        return
    
    


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        n = len(nums)
        i = n-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        left = i-1
        if left >= 0:
            j = n-1
            while j > left and nums[j] <= nums[left]:
                j -= 1
            
            nums[j], nums[left] = nums[left], nums[j]
            
        self.swapList(nums, i, n-1)
        return nums
    
        
        
    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
        return
    
    

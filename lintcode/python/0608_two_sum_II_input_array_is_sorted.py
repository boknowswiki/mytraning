#!/usr/bin/python -t

# two pointers
# time O(n)

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        n = len(nums)
        l = 0

        for r in range(n-1, -1, -1):
            while l < r and nums[l] + nums[r] < target:
                l += 1
                
            if l < r and nums[l] + nums[r] == target:
                return [l+1, r+1]
                
        return [-1, -1]
        
        

# binary search
# time O(nlogn)

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        n = len(nums)
        l = 0
        r = n-1
        
        while l < r:
            val = nums[l] + nums[r]
            if val == target:
                return [l+1, r+1]
            elif val < target:
                l += 1
            else:
                r -= 1
                
        return [-1,-1]
        
        

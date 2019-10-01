#!/usr/bin/python -t

# binary search, similar to 0824

class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def singleNonDuplicate(self, nums):
        # write your code here
        n = len(nums)
        l = 0
        r = n-1
        
        while l < r:
            mid = l + (r-l)/2
            if nums[mid] == nums[mid-1]:
                if (mid-l+1)%2 == 1:
                    r = mid-2
                else:
                    l = mid+1
            elif nums[mid] == nums[mid+1]:
                if (r-mid+1)%2 == 1:
                    l = mid+2
                else:
                    r = mid-1
            else:
                return nums[mid]
                
        return nums[l]


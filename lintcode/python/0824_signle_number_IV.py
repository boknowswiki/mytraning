#!/usr/bin/python -t

# binary search
# 二分长度，通过奇偶性找出落单的数

class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    def getSingleNumber(self, nums):
        # Write your code here
        n = len(nums)
        #nums.sort()
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            
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


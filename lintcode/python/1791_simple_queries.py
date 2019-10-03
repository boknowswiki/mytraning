#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param nums: 
    @param sub: 
    @return: return a Integer array
    """
    def SimpleQueries (self, nums, sub):
        # write your code here
        n = len(nums)
        if n == 0:
            return [0]*len(sub)
            
        ret = []
        nums.sort()
        
        for s in sub:
            if s < nums[0]:
                ret.append(0)
            elif s > nums[-1]:
                ret.append(n)
            else:
                index = self.upper_bound(nums, s)
                while index < n and nums[index] <= s:
                    index += 1
                ret.append(index)
                
        return ret
        
        
    def upper_bound(self, nums, target):
        l = 0
        r = len(nums)-1
        
        while l < r:
            mid = (l+r)/2
            if nums[mid] == target:
                return mid+1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
                
        return l


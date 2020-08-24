#!/usr/bin/python -t

class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """
    def splitArray(self, nums, m):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        if m > n:
            return 0
        if m == n:
            return max(nums)
            
        l = max(nums)
        r = sum(nums)
        
        while l +1< r:
            mid = l+(r-l)/2
            cnt = self.helper(nums, mid)
            print l, r, mid, cnt
            if cnt <= m:
                r = mid
            else:
                l = mid
        
        print l, r        
        if self.helper(nums, l) == m:
            return l
        return r
        
    def helper(self, nums, target):
        cnt = 0
        total = 0#nums[0]
        l = 0
        print target
        for i in range(len(nums)):
            total += nums[i]
            if total > target:
                cnt += 1
                total = nums[i]

        print cnt       
        return cnt+1

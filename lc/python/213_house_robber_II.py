#!/usr/bin/python -t

#Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.

#time O(n) space O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def myrob(nums, l, r):
            pre = cur = 0
            
            for i in range(l, r):
                tmp = max(pre+nums[i], cur)
                pre = cur
                cur = tmp
                
            return cur
        
        n = len(nums)
        if n < 2:
            return nums[0] if n != 0 else 0
        
        return max(myrob(nums, 0, n-1), myrob(nums, 1, n))

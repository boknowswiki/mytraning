#!/usr/bin/python -t

# sliding window time O(n) space O(1)

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        ret = index = 0
        
        for i in range(n):
            if i and nums[i-1] >= nums[i]:
                index = i
            ret = max(ret, i-index+1)
            
        return ret

# dp solution time O(n) space O(n)

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        ret = 1
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                ret = max(ret, dp[i])
                
        return ret

if __name__ =='__main__':
    s = [1,3,5,4,7]
    ss = Solution()
    print('answer is %r' % ss.findLengthOfLCIS(s))


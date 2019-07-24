#!/usr/bin/python -t

#dp my own solution
# time O(n^2)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 0:
            return 0
        
        dp = [0] * n
        max_val = 0
        
        for i in range(n):
            local_max = 0
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    local_max = max(local_max, dp[j])

            dp[i] = local_max+1
            #print dp
            max_val = max(max_val, dp[i])
                    
        return max_val

#other's solution
#from http://hawstein.com/2013/03/26/dp-novice-to-advanced/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 0:
            return 0
        
        dp = [0] * n
        max_val = 1
        
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    
                if dp[i] > max_val:
                    max_val = dp[i]
                    
        return max_val

#binary search, time O(nlogn) space O(n)
import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        ret = 0
        l = []
        
        for i in nums:
            index = bisect.bisect_left(l, i)
            if index >= len(l):
                l.append(i)
            else:
                l[index] = i
                
        return len(l)

#DP, time O(n^2) space O(n)

'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        l = [0]*n
        l[0] = 1
        ret = 0
        
        for i in range(n):
            max_val = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_val = max(max_val, l[j])
                    
            l[i] = max_val + 1
            ret = max(ret, l[i])
            
        return ret
'''

if __name__ == '__main__':
    s = Solution()
    ss = [10,9,2,5,3,7,101]
    print 'ret %d\n' % s.lengthOfLIS(ss)

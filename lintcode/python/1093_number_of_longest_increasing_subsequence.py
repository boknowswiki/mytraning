#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param nums: an array
    @return: the number of longest increasing subsequence
    """
    def findNumberOfLIS(self, nums):
        # Write your code here
        # dp[i] the max length we got at i
        # cnt[i] the max cnt we got at i
        
        n = len(nums)
        
        #each self is one length and one cnt at beginning
        dp = [1] * n
        cnt = [1] * n
        max_len = ret = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                        
            
            if max_len < dp[i]:
                max_len = dp[i]

        print dp
        print cnt
        for i in range(n):
            if dp[i] == max_len:
                ret += cnt[i]
                    
        return ret

if __name__ == '__main__':
    s = [1,3,5,4,7]
    s = [2,2,2,2,2]
    ss = Solution()
    print "answer is %d" % ss.findNumberOfLIS(s)

#!/usr/bin/python -t

# dp solution time O(mn) space O(n)

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def waysNCents(self, n):
        # write your code here
        # state: dp[i] the number of ways to representing with i cents
        # function: dp[i] += dp[i-cent[j]] for i >= cent[j]
        # init: dp[0] = 1
        # result dp[n]
        
        dp = [0] * (n+1)
        cent = [1, 5, 10, 25]
        dp[0] = 1
        
        for j in cent:
            for i in range(1, n+1):
                print i, j
                if i >= j:
                    dp[i] += dp[i-j]
                    print dp[i]
        #print dp
        return dp[n]

if __name__ == '__main__':
    s = 11
    ss = Solution()
    print "answer is %s" % ss.waysNCents(s)


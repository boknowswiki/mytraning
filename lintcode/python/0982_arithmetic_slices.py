#!/usr/bin/python -t

# dp solution, time O(n) space O(n)

class Solution:
    """
    @param A: an array
    @return: the number of arithmetic slices in the array A.
    """
    def numberOfArithmeticSlices(self, A):
        # Write your code here
        # dp[i] the number of arithmetic at A[i]
        # dp[i] = dp[i-1]+1 if A[i]-A[i-1] == A[i-1]-A[i-2]
        # dp[i] = 2 if A[i]-A[i-1] != A[i-1]-A[i-2]
        # ret = + dp[i] i in [2,n]
        
        n = len(A)
        if n <= 2:
            return 0
            
        dp = [0] * n
        
        for i in range(2, n):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 0
        print dp
                
        return sum(dp)

if __name__ == '__main__':
    s = [1,2,3,8,9,10]
    ss = Solution()
    print "answer is %s" % ss.numberOfArithmeticSlices(s)

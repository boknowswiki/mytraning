#!/usr/bin/python -t

class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        # state: dp[i] number of ways to decode it at ith point
        # function: dp[i] = dp[i-1] if 0<s[i] <= 9 and if 10<=(int(s[i-2])*10+int(s[i-1]))<= 26, dp[i] += dp[i-2]
        # init: dp[0] = 1
        # result: dp[n]
        
        n = len(s)
        if n == 0:
            return 0
            
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i >= 2:
                val = int(s[i-2])*10 + int(s[i-1])
                if 10 <= val <= 26:
                    dp[i] += dp[i-2]

        print dp
                
        return dp[n]

if __name__ == '__main__':
    s = "12"
    s = "1"
    s = "19261001"
    ss = Solution()
    print "answer is %s" % ss.numDecodings(s)

#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        # state: dp[i]: at wheter it can break into a space-separated sequence of one or more dictionary words at ith place
        # function: dp[i] = true when dp[i-j] is true and s[i-j:i] in the dictionary
        # init dp[0] = true
        # result dp[n]
        
        n = len(s)
        if len(dict) == 0:
            return n == 0
            
        dp = [False] * (n+1)
        dp[0] = True
        max_len = max(len(w) for w in dict)
        
        for i in range(1, n+1):
            for j in range(1, min(i, max_len)+1):
                # if previous is not true, then it's false
                if not dp[i-j]:
                    continue
                if s[i-j:i] in dict:
                    dp[i] = True
                    break
        print dp
        return dp[n]

if __name__ == '__main__':
    s= "a"
    k = ["a"]
    ss = Solution()
    print "answer is %s" % ss.wordBreak(s, k)

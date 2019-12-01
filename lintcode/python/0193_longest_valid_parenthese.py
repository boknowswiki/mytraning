#!/usr/bin/python -t

# dp

class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        # write your code here
        # dp[i] = dp[i+1]+2 and dp[i] += dp[j+1]
        
        n = len(s)
        if n <2:
            return 0
        
        dp = [0] * n
        ret = 0
        
        for i in range(n-2, -1, -1):
            if s[i] == '(':
                j = i+dp[i+1]+1
                if j < n and s[j] == ')':
                    dp[i] = dp[i+1]+2
                    
                    if j+1 < n:
                        dp[i] += dp[j+1]
                    ret = max(ret, dp[i])
                    
        return ret
            
        
#dp
#题解：
#一般对于最长XX问题容易想到利用DP求解，在这题中利用逆向DP，设状态dp[i]为从i到len - 1中，以i开头的最长合法子串长度：
#
#初始化：dp[len - 1] = 0
#如果s[i] = ')'，则跳过，因为不可能有由'('开头的串
#如果s[i] = '('，则需要找到右括号和它匹配，可以跳过以i + 1开头的合法子串，则需要看j = i + dp[i + 1] + 1是否为右括号。如果没越界且为右括号，那么有dp[i] = dp[i + 1] + 2，此外在这个基础上还要将j + 1开头的子串加进来（只要不越界）
# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        # write your code here
        if len(s) <= 1  :
            return 0
        res = 0
        dp = [0 for i in range(len(s))]     #初始化
        for i in range(len(s) - 2, -1, -1) :
            if s[i] == '(' :        #如果s[i] = '('，则需要找到右括号和它匹配
                j = i + dp[i + 1] + 1
                if j < len(s) and s[j] == ')' : #如果没越界且为右括号，那么有dp[i] = dp[i + 1] + 2
                    dp[i] = dp[i + 1] + 2
                    if j + 1 < len(s):          #还要将j + 1开头的子串加进来
                        dp[i] += dp[j + 1]
                res = max(res, dp[i])
        return res

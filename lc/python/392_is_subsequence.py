#!/usr/bin/python -t

#time O(logs*log(len(t)) space O(len(t))

from collections import defaultdict
from bisect import bisect_left

class Solution(object):
    def creat_map(self, s):
        m = defaultdict(list)
        for i , char in enumerate(s):
            m[char].append(i)
        return m
    
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = self.creat_map(t)
        low_bound = 0
        
        for i in s:
            if i not in m:
                return False
            
            index_list = m[i]
            index = bisect_left(index_list, low_bound)
            if index == len(index_list):
                return False
            low_bound = index_list[index] + 1
            
        return True


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False


#Time complexity: O(T + SlogT)

import collections
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = collections.defaultdict(list)
        for i in xrange(0, len(t)):
            d[t[i]].append(i)
        start = 0
        for c in s:
            idx = bisect.bisect_left(d[c], start)
            if len(d[c]) == 0 or idx >= len(d[c]):
                return False
            start = d[c][idx] + 1
        return True


#memory limit exceeded
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        if s[-1] == t[-1]:
            return self.isSubsequence(s[:-1], t[:-1])
        
        return self.isSubsequence(s, t[:-1])


#Many coders have provided the O<N, 1> 2-pointer solution.
#
#I am so bored so I came up with a dynamic programming solution for this problem.
#
#The recurrence is:
#
#dp(s, t) = dp(s, t-1) or ( S[s] = T[t] and dp(s-1, t-1) )
#
#Base case:
#
#dp(0, t) = true
#dp(s, 0) = (s == "")
#
#The complexity is O(N^2, N) lol

public class Solution {
    public boolean isSubsequence(String s, String t) {
        int sl = s.length();
        int tl = t.length();
        boolean [] dp = new boolean[sl+1];
        
        for(int i = 0; i <= tl; i ++) {
            for(int j = sl; j >= 0; j --) {
                if(j == 0) {
                    dp[j] = true;
                    continue;
                }
                
                if(i == 0) {
                    dp[j] = (j == 0);
                    continue;
                }
                
                dp[j] = dp[j] || (s.charAt(j-1) == t.charAt(i-1)) && dp[j-1];
            }
        }
        
        return dp[sl];
    }
}


#Dynamic Programming: O(n) space + O(m*n) time

public class Solution {
    public boolean isSubsequence(String s, String t) {
        boolean[] mem1 = new boolean[t.length()];
        boolean[] mem2 = new boolean[t.length()];
        if(s.length() == 0) return true;
        if(t.length() == 0) return false;
        mem1[0] = (s.charAt(0) == t.charAt(0));
        for(int j = 1; j < t.length(); j++)
        {
            mem1[j] = (s.charAt(0) == t.charAt(j))?true:mem1[j-1];
        }

        for(int i = 1 ; i < s.length() ; i++)
        {
            for(int j = 1 ; j < t.length(); j++)
            {
                if(s.charAt(i) == t.charAt(j))
                    mem2[j] = mem2[j-1] || mem1[j-1];
                else
                    mem2[j] = mem2[j-1];
            }
            mem1 = mem2;
            mem2 = new boolean[t.length()];
        }   
        return mem1[t.length()-1];
    }
}

# my own dp, TLE

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(t)
        n = len(s)
        if n == 0:
            return True
        if m == 0 or n > m:
            return False
        
        dp = [[False]*(n+1) for i in range(m+1)]
            
        for i in range(m+1):
            dp[i][0] = True
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] or ((t[i-1] == s[j-1]) and dp[i-1][j-1])
                    
        return dp[m][n]

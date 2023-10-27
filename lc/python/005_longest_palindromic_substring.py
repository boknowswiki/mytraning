#!/usr/bin/python -t

# dp
# time O(n^2)
# space O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp =[[False]*n for _ in range(n)]
        
        ans = [0, 0]
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]

        for diff in range(2, n):
            for i in range(n-diff):
                j = i+diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j+1]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        
        dp= [[0] * n for _ in xrange(n)]
        start = 0
        s_len = 1
        #base case
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j-i <3 or dp[i+1][j-1])
                if dp[i][j] and j-i+1 > s_len:
                    s_len = j-i+1
                    start = i
                    
                    
        return s[start:start+s_len]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_len = 0
        start = 0
        end = 0
        def expendfrom(s, l, r):
            while(l>=0 and r < len(s) and s[l] == s[r]):
                l = l - 1
                r = r + 1
            return r-l-1
        
        for i in range(n):
            len1 = expendfrom(s, i, i)
            len2 = expendfrom(s, i, i+1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len-1)/2
                end = i + max_len/2
                
        return s[start:end+1]

'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1

            return r - l - 1
        n = len(s)
        max_len = 0
        start = 0
        end = 0

        for i in xrange(n):
            len1 = expand(s, i, i)
            len2 = expand(s, i, i+1)
            max_len = max(len1, len2)
            if (max_len > end - start):
                start = i - (max_len - 1)/2
                end = i + (max_len)/2

        return s[start:end+1]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def ispalindrome(s):
            n = len(s)
            start = 0
            end = n - 1
            while start < end:
                if s[start] == s[end]:
                    start = start + 1
                    end = end - 1
                else:
                    return False

            return True

        n = len(s)
        max_len = 0
        ret = ""

        for i in xrange(n):
            for j in xrange(i, n, 1):
                #print '%s' % s[i:j+1]
                if ispalindrome(s[i:j+1]):
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        ret = s[i:j+1] 

        return ret


#Intuitively, we list all the substrings, pick those palindromic, and get the longest one. However, that causes TLE for we reach the same situations (input substrings) many times.
#To optimize, we decompose the problem as follows
#state variable:
#start index and end index of a substring can identify a state, which influences our decision
#so state variable is state(s, e) indicates whether str[s, e] is palindromic
#goal state:
#max(e - s + 1) that makes state(s, e) = true
#state transition:
#Let's observe example base cases
#for s = e, "a" is palindromic,
#for s + 1 = e, "aa" is palindromic (if str[s] = str[e])
#for s + 2 = e, "aba" is palindromic (if str[s] = str[e] and "b" is palindromic)
#for s + 3 = e, "abba" is palindromic (if str[s] = str[e] and "bb" is palindromic)
#we realize that
#for s + dist = e, str[s, e] is palindromic if str[s] == str[e] and str[s + 1, e - 1] is palindromic
#state transition equation:
#state(s, e) is true:
#for s = e, 
#for s + 1 = e,  if str[s] == str[e]
#for s + 2 <= e, if str[s] == str[e] && state(s + 1, e - 1) is true
#note:
#state(s + 1, e - 1) should be calculated before state(s, e). That is, s is decreasing during the bottop-up dp implementation, while the dist between s and e is increasing, that's why
#        for (int s = len - 1; s >= 0; s--) {
#            for (int dist = 1; dist < len - i; dist++) {
#We keep track of longestPalindromeStart, longestPalindromeLength for the final output.
#    public String longestPalindrome(String s) {
#        // Corner cases.
#        if (s.length() <= 1) return s;
#        int len = s.length(), longestPalindromeStart = 0, longestPalindromeLength = 1;
#        // state[i][j] true if s[i, j] is palindrome.
#        boolean[][] state = new boolean[len][len];
#        // Base cases.
#        for (int i = 0; i < len; i++) { 
#            state[i][i] = true; // dist = 0.
#        }
#        for (int i = len - 1; i >= 0; i--) {
#            for (int dist = 1; dist < len - i; dist++) {
#                int j = dist + i;
#                state[i][j] = (dist == 1) ? s.charAt(i) == s.charAt(j) : (s.charAt(i) == s.charAt(j)) && state[i + 1][j - 1];
#                if (state[i][j] && j - i + 1 > longestPalindromeLength) {
#                    longestPalindromeLength = j - i + 1;
#                    longestPalindromeStart = i;
#                }
#            }
#        }     
#        return s.substring(longestPalindromeStart, longestPalindromeStart + longestPalindromeLength);
#    }

#dp(i, j) represents whether s(i ... j) can form a palindromic substring, dp(i, j) is true when s(i) equals to s(j) and s(i+1 ... j-1) is a palindromic substring. When we found a palindrome, check if it's the longest one. Time complexity O(n^2).
#
#public String longestPalindrome(String s) {
#  int n = s.length();
#  String res = null;
#    
#  boolean[][] dp = new boolean[n][n];
#    
#  for (int i = n - 1; i >= 0; i--) {
#    for (int j = i; j < n; j++) {
#      dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i + 1][j - 1]);
#            
#      if (dp[i][j] && (res == null || j - i + 1 > res.length())) {
#        res = s.substring(i, j + 1);
#      }
#    }
#  }
#    
#  return res;
#}

'''

if __name__ =='__main__':
    s = Solution()
    print('%s\n' % (s.longestPalindrome("babad")))
    print('%s\n' % (s.longestPalindrome("cbbd")))

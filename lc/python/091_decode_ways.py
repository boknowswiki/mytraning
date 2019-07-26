#!/usr/bin/python -t

#dp solution, time O(n)

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n+1):
            tmp1 = int(s[i-1])
            tmp2 = int(s[i-2])

            if tmp1 > 0:
                dp[i] = dp[i-1]
            val = tmp2*10 + tmp1
            if 10 <= val <= 26:
                dp[i] += dp[i-2]
            
        return dp[n]

#Recursion O(2^n)
#    int numDecodings(string s) {
#        return s.empty() ? 0: numDecodings(0,s);    
#    }
#    int numDecodings(int p, string& s) {
#        int n = s.size();
#        if(p == n) return 1;
#        if(s[p] == '0') return 0;
#        int res = numDecodings(p+1,s);
#        if( p < n-1 && (s[p]=='1'|| (s[p]=='2'&& s[p+1]<'7'))) res += numDecodings(p+2,s);
#        return res;
#    }
#Memoization O(n)
#    int numDecodings(string s) {
#        int n = s.size();
#        vector<int> mem(n+1,-1);
#        mem[n]=1;
#        return s.empty()? 0 : num(0,s,mem);   
#    }
#    int num(int i, string &s, vector<int> &mem) {
#        if(mem[i]>-1) return mem[i];
#        if(s[i]=='0') return mem[i] = 0;
#        int res = num(i+1,s,mem);
#        if(i<s.size()-1 && (s[i]=='1'||s[i]=='2'&&s[i+1]<'7')) res+=num(i+2,s,mem);
#        return mem[i] = res;
#    }
#dp O(n) time and space, this can be converted from #2 with copy and paste.
#    int numDecodings(string s) {
#        int n = s.size();
#        vector<int> dp(n+1);
#        dp[n] = 1;
#        for(int i=n-1;i>=0;i--) {
#            if(s[i]=='0') dp[i]=0;
#            else {
#                dp[i] = dp[i+1];
#                if(i<n-1 && (s[i]=='1'||s[i]=='2'&&s[i+1]<'7')) dp[i]+=dp[i+2];
#            }
#        }
#        return s.empty()? 0 : dp[0];   
#    }
#dp constant space
#    int numDecodings(string s) {
#        int p = 1, pp, n = s.size();
#        for(int i=n-1;i>=0;i--) {
#            int cur = s[i]=='0' ? 0 : p;
#            if(i<n-1 && (s[i]=='1'||s[i]=='2'&&s[i+1]<'7')) cur+=pp;
#            pp = p;
#            p = cur;
#        }
#        return s.empty()? 0 : p;   
#    }

int numDecodings(string s) {
    if (!s.size() || s.front() == '0') return 0;
    // r2: decode ways of s[i-2] , r1: decode ways of s[i-1] 
    int r1 = 1, r2 = 1;
    
    for (int i = 1; i < s.size(); i++) {
        // zero voids ways of the last because zero cannot be used separately
        if (s[i] == '0') r1 = 0;

        // possible two-digit letter, so new r1 is sum of both while new r2 is the old r1
        if (s[i - 1] == '1' || s[i - 1] == '2' && s[i] <= '6') {
            r1 = r2 + r1;
            r2 = r1 - r2;
        }

        // one-digit letter, no new way added
        else {
            r2 = r1;
        }
    }

    return r1;
}

#time O(n) space O(n)
#myself solution

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def dfs(s, index, dp):
            def isvalid(ss):
                if len(ss) == 0:
                    return False
                if ss[0] == '0':
                    return False
                return 1 <= int(ss) <= 26
            
            if index >= len(s):
                return 1
            
            if dp[index] != 0:
                return dp[index]
            
            for i in (index, len(s)):
                if isvalid(s[index:index+1]):
                    len1 = dfs(s, index+1, dp)
                else:
                    len1 = 0
                if index+2 <= len(s) and isvalid(s[index:index+2]):
                    len2 = dfs(s, index+2, dp)
                else:
                    len2 = 0
                    
                dp[index] = len1 + len2
                
            return dp[index]
            
        n = len(s)
        dp = [0] * (n+1)
        
        return dfs(s, 0, dp)


#I used a dp array of size n + 1 to save subproblem solutions. dp[0] means an empty string will have one way to decode, dp[1] means the way to decode a string of size 1. I then check one digit and two digit combination and save the results along the way. In the end, dp[n] will be the end result.
#
#public class Solution {
#    public int numDecodings(String s) {
#        if(s == null || s.length() == 0) {
#            return 0;
#        }
#        int n = s.length();
#        int[] dp = new int[n+1];
#        dp[0] = 1;
#        dp[1] = s.charAt(0) != '0' ? 1 : 0;
#        for(int i = 2; i <= n; i++) {
#            int first = Integer.valueOf(s.substring(i-1, i));
#            int second = Integer.valueOf(s.substring(i-2, i));
#            if(first >= 1 && first <= 9) {
#               dp[i] += dp[i-1];  
#            }
#            if(second >= 10 && second <= 26) {
#                dp[i] += dp[i-2];
#            }
#        }
#        return dp[n];
#    }
#}


if __name__ =='__main__':
    s = "12"
    ss = Solution()
    print('answer is %d' % ss.numDecodings(s))

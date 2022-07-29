#!/usr/bin/python3 -t

# dfs with memorization
# time O(n*2^n)
# space O(n)

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        if not s:
            return []

        return self.dfs(s, {})

    def dfs(self, s, memo):
        if not s:
            return []
        if s in memo:
            return memo[s]

        parts = []

        for i in range(len(s)-1):
            prefix = s[:i+1]
            if not self.is_palindrome(prefix):
                continue

            sub_parts = self.dfs(s[i+1:], memo)
            for p in sub_parts:
                parts.append([prefix]+p)

        if self.is_palindrome(s):
            parts.append([s])

        memo[s] = parts
        return parts

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    a = "a"
    a = "aab"
    print(s.partition(a))

# dfs
# time O(2^n)

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        ret = []
        
        self.dfs(s, 0, [], ret)
        
        return ret
        
    def dfs(self, s, start, com, ret):
        if start == len(s):
            ret.append(list(com))
            return
        
        for i in range(start, len(s)):
            ss = s[start:i+1]
            
            if self.isPalindrome(ss):
                com.append(ss)
                self.dfs(s, i+1, com, ret)
                com.pop()
                
        return
    
    def isPalindrome(self, s):
        
        return s == s[::-1]
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
                
            i += 1
            j -= 1
            
        return True



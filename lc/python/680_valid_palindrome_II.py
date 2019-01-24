#!/usr/bin/python -t

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_sub_pali(i, j):
            #return all(s[k] == s[j-k+i] for k in range(i,j))
            while i < j:
                if s[i] != s[j]:
                    return False
                else:
                    i = i + 1
                    j = j - 1
                    
            return True
        
        for i in range(len(s)/2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_sub_pali(i, j-1) or is_sub_pali(i+1, j)
            
        return True


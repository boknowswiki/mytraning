#!/usr/bin/python -t

# two pointers

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True

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


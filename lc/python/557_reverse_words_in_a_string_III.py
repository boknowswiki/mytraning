#!/usr/bin/python -t

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        new_s = s[::-1]
        j = n
        ret = ''
        for i in range(n-1, -1, -1):
            if s[i] == ' ':
                j = i
            elif i == 0 or s[i-1] == ' ':
                if len(ret) != 0:
                    ret = ret + ' '
                ret = ret + s[i:j]
                
        ret = ret[::-1]
        return ret


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ret = ''
        i = 0
        
        while i < n:
            j = i
            while i < n and s[i] != ' ':
                i = i + 1
                
            if j < i:
                word = s[j:i]
                ret = ret + word[::-1] + ' '
                
            while i < n and s[i] == ' ':
                i = i + 1
            
        ret = ret[:-1]
        return ret

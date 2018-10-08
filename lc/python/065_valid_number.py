#!/usr/bin/python -t

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i = 0
        while i < n and s[i] == ' ':
            i = i + 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            i = i + 1

        isnumber = False

        while i < n and s[i].isdigit():
            i = i + 1
            isnumber = True

        if i < n and s[i] == '.':
            i = i + 1
            while i < n and s[i].isdigit():
                i = i + 1
                isnumber = True

        if isnumber and i < n and s[i] == 'e':
            i = i + 1
            isnumber = False
            if i < n and (s[i] == '+' or s[i] == '-'):
                i = i + 1
            while i < n and s[i].isdigit():
                i = i + 1
                isnumber = True

        while i < n and s[i] == ' ':
            i = i + 1

        return isnumber and i == n


#!/usr/bin/python -t

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        d = {"(": ")", "[": "]", "{": "}"}

        for i in s:
            if i in d:
                st.append(i)
            elif not st or d[st.pop()] != i:
                return False

        return True if not st else False


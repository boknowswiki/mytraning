#!/usr/bin/python -t

# two pointers and string
# time O(n)
# space O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        
        new_s = ""
        
        i = len(s)-1
        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue
            start = i
            while i >= 0 and s[i] != " ":
                i -= 1
            end = i+1
            word = s[end:start+1]
            if new_s == "":
                new_s += word
            else:
                new_s += " " + word
                
        return new_s

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return s

        new_s = ''
        i = 0
        # remove head spaces
        while i < n and s[i] == ' ':
            i = i + 1
        while i < n:
            start = i
            while i < n and s[i] != ' ':
                i = i + 1
            if start < i:
                word = s[start:i]
                new_s = new_s + word[::-1] + ' '
            i = i + 1

        new_s = new_s[:-1]
        new_s = new_s[::-1]

        return new_s


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        new_s = ''
        j = n
        for i in range(n-1, -1, -1):
            if s[i] == ' ':
                j = i
            elif i == 0 or s[i-1] == ' ':
                if len(new_s) != 0:
                    new_s = new_s + ' '
                new_s = new_s + s[i:j]
                #print s[i:j]
                #print new_s

        return new_s

if __name__ =='__main__':
    s = Solution()
    print('%s\n' % (s.reverseWords("the sky is blue")))


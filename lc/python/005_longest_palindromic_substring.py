#!/usr/bin/python -t

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

if __name__ =='__main__':
    s = Solution()
    print('%s\n' % (s.longestPalindrome("babad")))
    print('%s\n' % (s.longestPalindrome("cbbd")))

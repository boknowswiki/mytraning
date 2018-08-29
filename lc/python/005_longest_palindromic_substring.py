#!/usr/bin/python -t

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

if __name__ =='__main__':
    s = Solution()
    print('%s\n' % (s.longestPalindrome("babad")))
    print('%s\n' % (s.longestPalindrome("cbbd")))

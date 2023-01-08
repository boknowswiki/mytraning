#!/usr/bin/python -t

# hash map
# time O(n)
# space O(1) if char set is small and can be instant

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index is not None and left <= index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res

# hash map
# time O(n)
# space O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        window = dict()
        ret = 0
        l = 0

        for r in range(n):
            if s[r] in window:
                while l < r and s[r] in window:
                    del window[s[l]]
                    l += 1
            window[s[r]] = r
            ret = max(ret, r-l+1)

        return ret

#time O(n) space O(n)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        max_len = 0
        i = 0
        d = {}
        
        for j in range(n):
            if s[j] in d:
                i = max(i, d[s[j]] + 1)
            d[s[j]] = j
            max_len = max(max_len, j-i+1)
        return max_len



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        l = [0] *256
        i = 0
        max_len = 0
        
        for j in range(n):
            while l[ord(s[j])] == 1:
                l[ord(s[i])] = 0
                i = i + 1
            l[ord(s[j])] = 1
            max_len = max(max_len, j-i+1)
            
        return max_len



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        d = {}
        max_len = 0
        cur_max = 0

        for i in range(n):
            if s[i] in d:
                cur_len = i-d[s[i]]
                #cur_max = max(cur_max, cur_len)
                if cur_len > cur_max:
                    cur_max = cur_len
                d[s[i]] = i
            else:
                d[s[i]] = i
                cur_max = cur_max + 1

            max_len = max(max_len, cur_max)

        return max_len

if __name__ == '__main__':
    s = Solution()
    print('%d\n' % (s.lengthOfLongestSubstring("pwwkew")))

                

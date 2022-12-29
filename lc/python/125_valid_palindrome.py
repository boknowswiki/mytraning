#!/usr/bin/python -t

# two pointers
# time O(n)
# space O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        n = len(s)
        l = 0
        r = n-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if l == r:
                break
            if s[l].lower() != s[r].lower():
                #print(f"{s[l]}, {s[r]}")
                return False
            l += 1
            r -= 1

        return True

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        start = 0
        end = n - 1
        lower_s = s.lower()
        while start < end:
            while (start < end) and (not lower_s[start].isalnum()):
                start = start + 1
            while (start < end) and (not lower_s[end].isalnum()):
                end = end - 1
            if lower_s[start] == lower_s[end]:
                start = start + 1
                end = end - 1
            else:
                return False
            
        return True

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0 or n == 1:
            return True

        new_s = s.lower()
        start = 0
        end = n - 1

        while start < end:
            while start < end and (new_s[start].isalnum() != True): 
                start = start + 1
            while start < end and (new_s[end].isalnum() != True): 
                end = end - 1
            if ord(new_s[start]) == ord(new_s[end]):
                start = start + 1
                end = end - 1
            else:
                #print "%s, %s" % (s[start], s[end])
                return False

        return True

if __name__ =='__main__':
    s = Solution()
    #print('%s\n' % (s.isPalindrome("A man, a plan, a canal: Panama")))
    print('%s\n' % (s.isPalindrome("0P")))


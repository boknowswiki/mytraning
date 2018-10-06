#!/usr/bin/python -t

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def reverse(s, start, end):
            print s, start, end
            while start < end:
                s[start], s[end] = s[end], s[start]
                start = start + 1
                end = end - 1
            print s

            return
        n = len(s)
        reverse(s, 0, n-1)
        print s
        i = 0
        while i < n:
            j = i
            while i < n and s[i] != ' ':
               i = i + 1

            reverse(s, j, i-1)
            i = i + 1

        return s

if __name__ =='__main__':
    s = ['h','e','l','l','o', ' ', 'w', 'o', 'r', 'l', 'd']
    Solution().reverseWords(s)
    print(s)


'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        ls, pos = len(s), 0
        if s is None or ls == 0:
            return
        self.reverse(s, 0, ls)
        for i in range(ls + 1):
            if i == ls or s[i] == ' ':
                self.reverse(s, pos, i)
                pos = i + 1

    def reverse(self, array_s, begin, end):
        for i in range((end - begin) / 2):
            array_s[begin + i], array_s[end - i - 1] = array_s[end - i - 1], array_s[begin + i]
'''

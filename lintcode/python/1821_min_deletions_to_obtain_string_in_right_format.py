#!/usr/bin/python -t

class Solution:
    """
    @param s: the string
    @return: Min Deletions To Obtain String in Right Format
    """
    def minDeletionsToObtainStringInRightFormat(self, s):
        # write your code here
        n = len(s)

        # at index i, there are count_A of A after index i, count_B of B before index i to make all A before all B.
        count_A = 0
        count_B = 0

        for c in s:
            if c == 'A':
                count_A += 1

        # max delete number of letters.
        ret = count_A

        for c in s:
            if c == 'A':
                count_A -= 1
            else:
                count_B += 1

            ret = min(ret, count_A+count_B)

        return ret

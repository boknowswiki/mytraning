#!/usr/bin/python -t

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)

        #swap s and t, if len(s) > len(t)
        if m > n:
            return self.isOneEditDistance(t, s)

        if n - m > 1:
            return False

        i = 0
        shift = n - m

        #append case
        while i < m and s[i] == t[i]:
            i = i + 1

        if i == m:
            return shift > 0

        #modify case
        if shift == 0:
            i = i + 1

        #insert case
        while i < m and s[i] == t[i+shift]:
            i = i + 1

        return i == m


def edit_distance(s, t, m, n):
    if m > n:
        return edit_distance(t, s, n, m)

    if m == 0:
        return n

    if n == 0:
        return m

    if s[m-1] = t[n-1]:
        return edit_distance(s, t, m-1, n-1)

    return 1 + min(edit_distance(s, t, m, n-1),
                    edit_distance(s, t, m-1, n),
                    edit_distance(s, t, m-1, n-1))

def one_edit_distance(s,t):
    return edit_distance(s, t, len(s), len(t)) == 1


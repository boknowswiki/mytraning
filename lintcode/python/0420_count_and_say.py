#!/usr/bin/python -t

# string

class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """
    def countAndSay(self, n):
        # write your code here

        s = "1"

        for i in range(1, n):

            s = self.readString(s)

        return s

    def readString(self, s):

        count = 0
        string = ""

        for i in range(len(s)):

            if i == 0 or s[i] == s[i - 1]:

                count += 1

            else:

                string += str(count) + "" + s[i - 1]

                count = 1

        string += str(count) + "" + s[len(s) - 1]

        return string

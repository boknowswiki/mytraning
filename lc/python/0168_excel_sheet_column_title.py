# string
# time O(logn)
# space O(n)

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ""

        while columnNumber > 0:
            columnNumber -= 1
            ret += (chr(ord("A")+(columnNumber % 26)))
            columnNumber //= 26

        return ret[::-1]

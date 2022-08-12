#!/usr/bin/python -t

# string
# time O(n)
# space O(1)

class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def rotate_string2(self, str: str, left: int, right: int) -> str:
        # write your code here
        n = len(str)
        if n == 0 or left == right:
            return str

        left = left % n
        right = right % n
        ret = ""
        if left > right:
            move_left = left - right
            ret = str[move_left:] + str[:move_left]
        else:
            move_right = right - left
            ret = str[-move_right:] + str[:-move_right]

        return ret

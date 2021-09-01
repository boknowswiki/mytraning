#!/usr/bin/python -t

# 首先loop一遍找到一个人i使得对于所有j(j>=i)都不认识i。
# 然后再loop一遍判断是否有人不认识i或者i认识某个人。

"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        if n == 0:
            return -1

        cele = 0

        for i in range(1, n):
            if Celebrity.knows(cele, i):
                cele = i

        for i in range(n):
            if i == cele:
                continue
            if Celebrity.knows(cele, i):
                return -1

            if not Celebrity.knows(i, cele):
                return -1

        return cele

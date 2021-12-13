#!/usr/bin/python -t

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):
        # write your code here
        if l1.x > r2.x or l2.x > r1.x:
            return False

        if l1.y < r2.y or l2.y < r1.y:
            return False
        
        return True

"""
Definition for a point.
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):
        # write your code here
        tl, tr, bl, br = self.getPoints(l1, r1)
        if self.inRange(l2, r2, tl):
            return True
        if self.inRange(l2, r2, tr):
            return True
        if self.inRange(l2, r2, bl):
            return True
        if self.inRange(l2, r2, br):
            return True
        return False

    def inRange(self, l2, r2, p):
        if l2[0] <= p.x <= r2[0]:
            return True
        if l2[1] <= p.y <= r2[1]:
            return True
        return False
        
    def getPoints(self, l1, r1):
        tl = Point(l1[0], l1[1])
        tr = Point(r1[0], l1[1])
        bl = Point(l1[0], r1[1])
        br = Point(r1[0], r1[1])
        return tl, tr, bl, br
        


if __name__ == '__main__':
    s = Solution()
    '''
    l1 = [0, 8]
    r1 = [8, 0]
    l2 = [6, 6]
    r2 = [10, 0]
    '''
    l1 = [0, 8]
    r1 = [8, 0]
    l2 = [9, 6]
    r2 = [10, 0]
    print(s.doOverlap(l1, r1, l2, r2))
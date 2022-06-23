#!/usr/bin/python3 -t

# binary search
# time O(nlogm + mlogn)
# space O(1)

# can improve the code by find_lower and find_higher with col or row to call
# empty_col or empty_row accordingly.

from typing import (
    List,
)

class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def min_area(self, image: List[List[str]], x: int, y: int) -> int:
        # write your code here
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        if n == 0:
            return 0

        left = self.find_left(image, 0, y)
        right = self.find_right(image, y, n-1)
        top = self.find_top(image, 0, x)
        bottom = self.find_bottom(image, x, m-1)

        #print(f"{left}, {right}, {top}, {bottom}")
        return (right-left+1) * (bottom-top+1)

    def find_left(self, image, start, end):
        m, n = len(image), len(image[0])

        while start + 1 < end:
            mid = start + (end-start)//2
            if self.empty_col(image, mid):
                start = mid
            else:
                end = mid

        #print(f"{start}, {end}")
        if not self.empty_col(image, start):
            return start

        return end

    def find_right(self, image, start, end):
        m, n = len(image), len(image[0])

        while start + 1 < end:
            mid = start + (end-start)//2
            if self.empty_col(image, mid):
                end = mid
            else:
                start = mid

        if not self.empty_col(image, end):
            return end

        return start

    def find_top(self, image, start, end):
        m, n = len(image), len(image[0])

        while start + 1 < end:
            mid = start + (end-start)//2
            if self.empty_row(image, mid):
                start = mid
            else:
                end = mid

        if not self.empty_row(image, start):
            return start

        return end

    def find_bottom(self, image, start, end):
        m, n = len(image), len(image[0])

        while start + 1 < end:
            mid = start + (end-start)//2
            if self.empty_row(image, mid):
                end = mid
            else:
                start = mid

        if not self.empty_row(image, end):
            return end

        return start

    def empty_col(self, image, col):
        m, n = len(image), len(image[0])
        for i in range(m):
            #print(f"empty col {col}, {image[i][col]}")
            if image[i][col] == "1":
                return False

        return True

    def empty_row(self, image, row):
        m, n = len(image), len(image[0])
        for i in range(n):
            if image[row][i] == "1":
                return False

        return True

if __name__ == '__main__':
    s = Solution()
    a = ["0010","0110","0100"]
    b = 0
    c = 2
    print(s.min_area(a, b, c))

# binary search
# time nlog(m) + mlog(n)

class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        m = len(image)
        if m == 0:
            return 0
            
        n = len(image[0])
        if n == 0:
            return 0
        
        left = self.findLeft(image, m, n, 0, y)
        right = self.findRight(image, m, n, y, n-1)
        top = self.findTop(image, m, n, 0, x)
        bottom = self.findBottom(image, m, n, x, m-1)
        
        return (right-left+1) * (bottom-top+1)
        
        
    def emptyCol(self, image, m, n, mid):
        for i in range(m):
            if image[i][mid] == '1':
                return False
        return True
        
    def emptyRow(self, image, m, n, mid):
        for i in range(n):
            if image[mid][i] == '1':
                return False
        return True
            
    def findLeft(self, image, m, n, l, r):
        while l+1 < r:
            mid = (l+r)/2
            #print "left"
            #print mid, l, r
            if self.emptyCol(image, m, n, mid):
                l = mid
            else:
                r = mid
                
        if self.emptyCol(image, m, n, l):
            return r
        return l
        
    def findRight(self, image, m, n, l, r):
        while l+1 < r:
            mid = (l+r)/2
            #print "right"
            #print mid, l, r
            if self.emptyCol(image, m, n, mid):
                r = mid
            else:
                l = mid
                
        if self.emptyCol(image, m, n, r):
            return l
        return r
        
    def findTop(self, image, m, n, l, r):
        while l+1< r:
            mid = (l+r)/2
            #print "top"
            #print mid, l, r
            if self.emptyRow(image, m, n, mid):
                l = mid
            else:
                r = mid
                
        if self.emptyRow(image, m, n, l):
            return r
                
        return l
        
    def findBottom(self, image, m, n, l, r):
        while l+1 < r:
            mid = (l+r)/2
            #print "bot"
            #print mid, l, r
            if self.emptyRow(image, m, n, mid):
                r = mid
            else:
                l = mid
                
        if self.emptyRow(image, m, n, r):
            return l
        return r
        
                    

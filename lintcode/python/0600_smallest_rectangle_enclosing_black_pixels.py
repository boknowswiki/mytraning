#!/usr/bin/python -t

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
        
                    

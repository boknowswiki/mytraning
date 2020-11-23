#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param a: array a
    @param b: the query array
    @return: Output an array of length `b.length` to represent the answer
    """
    def minimalDistance(self, a, b):
        # Write your code here 
        self.quicksort(a, 0, len(a)-1)
        ret = []
        
        print a
        for c in b:
            ret.append(self.lower(a, c))
            
        return ret
        
    def quicksort(self, a, start, end):
        if start < end:
            part = self.partition(a, start, end)
            self.quicksort(a, start, part-1)
            self.quicksort(a, part+1, end)
            
            return
        
    def partition(self, a, start, end):
        pivot = a[end]
        i = start
        
        for j in range(start, end):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[end] = a[end], a[i]
        return i
        
    def lower(self, a, c):
        l = 0
        r = len(a)-1
        
        while l +1 < r:
            mid = l + (r-l)/2
            if a[mid] == c:
                return a[mid]
            elif a[mid] < c:
                l = mid
            else:
                r = mid
                
        if abs(a[l]-c) <= abs(a[r]-c):
            return a[l]
        
        return a[r]

class Solution:
    """
    @param a: array a
    @param b: the query array
    @return: Output an array of length `b.length` to represent the answer
    """
    def minimalDistance(self, a, b):
        # Write your code here
        ret = b
        n = len(a)
        m = len(b)
        a.sort()
        
        for i in range(m):
            id = self.lower_bound(a, b[i])
            if id == 0:
                ret[i] = a[id]
            elif id == n:
                ret[i] = a[id-1]
            else:
                if (b[i] - a[id - 1] <= a[id] - b[i]):
                    ret[i] = a[id - 1]
                else:
                    ret[i] = a[id]
        return ret

    def lower_bound(self, a, val):
        n = len(a)
        l = 0
        r = n-1
        while l < r:
            mid = (l+r)/2
            if a[mid] < val:
                l = mid +1
            else:
                r = mid
                
        return l


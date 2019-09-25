#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        size = len(A)
        sums = [0] * (size + 1)
        for i in range(size):
            sums[i] = sums[i - 1] + A[i]
        
        result = 0
        for i in range(size):
            # bisect left
            lo, hi = i, size
            while lo < hi:
                mid = (lo + hi) // 2
                if sums[mid] - sums[i - 1] < start:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == size: break
            left = lo
            
            # bisect right
            lo, hi = i, size
            while lo < hi:
                mid = (lo + hi) // 2
                if sums[mid] - sums[i - 1] > end:
                    hi = mid
                else:
                    lo = mid + 1
            #if lo == i and A[i] > size:
            #    continue
            right = lo
                  
            result += right - left
            
        return result


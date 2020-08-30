#!/usr/bin/python -t

class Solution:
    """
    @param sweetness: an integer array
    @param K: an integer
    @return:  return the maximum total sweetness of the piece
    """
    def maximizeSweetness(self, sweetness, K):
        # write your code here
        n = len(sweetness)
        if n <= K:
            return 0
        l = min(sweetness)
        r = sum(sweetness)
        
        while l + 1 < r:
            mid = (l+r)/2
            if self.helper(sweetness, K, mid):
                l = mid
            else:
                r = mid
                
        #print l, r
        if self.helper(sweetness, K, r):
            return r
        return l
        
    def helper(self, sweetness, K, target):
        cnt = 0
        total = 0
        
        for i in range(len(sweetness)):
            total += sweetness[i]
            if cnt == K:
                continue
            if total >= target:
                total = 0
                cnt += 1
                
        if cnt == K and total >= target:
            return True
        return False
        

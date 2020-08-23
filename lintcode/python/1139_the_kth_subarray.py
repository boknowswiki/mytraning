#!/usr/bin/python -t

class Solution:
    """
    @param a: an array
    @param k: the kth
    @return: return the kth subarray
    """
    def thekthSubarray(self, a, k):
        # wrrite your code here
        n = len(a)
        if n == 0:
            return 0
            
        l = min(a)
        r = sum(a)
        
        while l +1 < r:
            mid = l + (r-l)/2
            cnt = self.helper(a, mid)
            #print l, r, mid, cnt
            if cnt < k:
                l = mid
            else:
                r = mid
                
        #print l, r, self.helper(a, l)
        if self.helper(a, l) >= k:
            return l
        return r
        
    def helper(self, a, target):
        cnt = 0
        subsum = a[0]
        l = 0
        r = 0
        n = len(a)
        total = n * (n + 1) / 2
        #  l++ cond >> False 
        #  r++ cond >> True 
        while  r < n:
            if subsum > target:
                cnt += n - r 
                subsum -= a[l]
                l += 1
            else:
                r += 1
                if r < n:
                    subsum += a[r]
                else:
                    break
        return total - cnt     

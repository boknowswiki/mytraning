
# binary search

class Solution:
    """
    @param A: a list of integers
    @param K: a integer
    @return: return two integers
    """
    def kthSmallestPrimeFraction(self, A, K):
        # write your code here
        if A is None or K is None:
            return [0, 0]
            
        l = 0.0
        r = 1.0
        ret = [0, 0]
        
        while r - l > 1e-9:
            mid = (l+r)/2
            cnt, ans = self.helper(mid, A)
            #print cnt, ans, l, r, mid
            if cnt == K:
                return ans
            elif cnt < K:
                l = mid
            else:
                r = mid
                ret = ans
                
        return ret
        
    def helper(self, target, A):
        cnt = 0
        i = -1
        ret = [0, None, None]
        for j in range(1, len(A)):
            while A[i+1] < A[j]*target:
                i += 1
                
            #print cnt, i, j
            cnt += i+1
            if i >= 0:
                ans = [float(A[i])/A[j], A[i], A[j]]
                if ans[0] > ret[0]:
                    ret = ans
                    #print ret
                
        return cnt, ret[1:]



#heap hit memory limit exceeded error


import heapq

class Solution:
    """
    @param A: a list of integers
    @param K: a integer
    @return: return two integers
    """
    def kthSmallestPrimeFraction(self, A, K):
        # write your code here
        if A is None or K is None:
            return []
        hq = []
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                cur = (-float(A[i])/A[j], A[i], A[j])
                #print cur
                heapq.heappush(hq, cur)
                #print hq
                if len(hq) == K+1:
                    heapq.heappop(hq)
                    
        ret = heapq.heappop(hq)
        
        return [ret[1], ret[2]]


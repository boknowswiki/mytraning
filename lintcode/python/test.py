#!/usr/bin/python -t



import heapq

class Solution:
    """
    @param nums: a list of integers
    @param k: a integer
    @return: return a integer
    """
    def smallestDistancePair(self, nums, k):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        hq = []
        nums.sort()
        print nums
        
        for i in range(1, n):
            print i, hq
            if len(hq) >= k:
                break
            for j in range(n-i):
                for l in range(j+1, j+1+i):
                    
                    diff = nums[l]-nums[j]
                    print j, l, diff
                    if diff < 0:
                        print "error diff", diff
                    heapq.heappush(hq, -diff)
                    print hq
                    if len(hq) == k+1:
                        heapq.heappop(hq)
              
        print "outside"
        print len(hq)
        #heapq.heappop(hq)
        while len(hq) > k:
            print "in loop"
            val =heapq.heappop(hq)
            print val
        print hq
        return hq[0]

if __name__ == "__main__":
    nums = [9,10,7,10,6,1,5,4,9,8]
    k = 18
    s = Solution()
    r = s.smallestDistancePair(nums, k)
    print r

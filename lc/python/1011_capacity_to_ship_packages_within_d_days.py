#!/usr/bin/python -t

# binary search

# time O(nlogn)
# space O(1)

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def get_days(target):
            cnt = 1
            cur = 0
            for w in weights:
                cur += w
                if cur > target:
                    cnt += 1
                    cur = w

            return cnt

        while l < r:
            mid = l + (r-l)//2
            need = get_days(mid)
            if need > days:
                l = mid+1
            else:
                r = mid

        return l

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        l, r = max(weights), sum(weights)
        
        while l < r:
            mid, need, cur = l + (r-l)/2, 1, 0
            
            for w in weights:
                if cur + w > mid:
                    need = need + 1
                    cur = 0
                cur = cur + w
                
            if need > D:
                l = mid + 1
            else:
                r = mid
        
        return l

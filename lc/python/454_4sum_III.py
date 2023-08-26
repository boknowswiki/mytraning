#!/usr/bin/python -t

# hash table
# time O(n^2)
# space O(n)

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        m = collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                m[a + b] += 1
                
        for c in nums3:
            for d in nums4:
                cnt += m[-(c + d)]
                
        return cnt

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        h = {}
        for a in A:
            for b in B:
                if a+b in h:
                    h[a+b] += 1
                else:
                    h[a+b] = 1
                    
        count = 0
        
        for c in C:
            for d in D:
                if -c-d in h:
                    count += h[-c-d]
                    
        return count


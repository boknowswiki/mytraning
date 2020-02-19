#!/usr/bin/python -t

# heap
# heap: every time calling heapq.heappop(), use heapq.heappush() to add next valid one
# time O(klonk)



import heapq

class Solution:
    """
    @param nums1: List[int]
    @param nums2: List[int]
    @param k: an integer
    @return: return List[List[int]]
    """
    def kSmallestPairs(self, nums1, nums2, k):
        # write your code here
        n1 = len(nums1)
        n2 = len(nums2)
        heap = [(nums1[0]+nums2[0], 0, 0)]
        seen = {(0, 0)}
        ret = []
        
        for i in range(min(k, n1*n2)):
            _, index1, index2 = heapq.heappop(heap)
            ret.append([nums1[index1], nums2[index2]])
            
            if index1 + 1 < n1 and (index1+1, index2) not in seen:
                heapq.heappush(heap, (nums1[index1+1]+nums2[index2], index1+1, index2))
                seen.add((index1+1, index2))
            if index2 + 1 < n2 and (index1, index2+1) not in seen:
                heapq.heappush(heap, (nums1[index1]+nums2[index2+1], index1, index2+1))
                seen.add((index1, index2+1))
                
        return ret
        


# heap
# 简单heap方法，将n1+n2, n1, n2 无脑放入最小堆，最后从堆中pop出k个即可
# time O(mn) space O(m+n)


import heapq

class Solution:
    """
    @param nums1: List[int]
    @param nums2: List[int]
    @param k: an integer
    @return: return List[List[int]]
    """
    def kSmallestPairs(self, nums1, nums2, k):
        # write your code here
        heap = []
        
        ret = []
        
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(heap, (num1+num2, num1, num2))
                
        for _ in range(min(k, len(heap))):
            _, num1, num2 = heapq.heappop(heap)
            ret.append([num1, num2])
            
        return ret
        

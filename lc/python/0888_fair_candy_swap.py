#!/usr/bin/python -t

# hash map, tagged with binary search
# time O(m+n), m = len(aliceSizes), n = len(bobSizes)
# space O(n)
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a, sum_b = sum(aliceSizes), sum(bobSizes)
        set_b = set(bobSizes)
        
        for c in aliceSizes:
            if c + (sum_b - sum_a)//2 in set_b:
                return [c, c+(sum_b-sum_a)//2]

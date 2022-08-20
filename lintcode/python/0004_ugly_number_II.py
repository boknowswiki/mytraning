#!/usr/bin/python -t

# heap
# time O(nlogn)
# space O(n)


import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nth_ugly_number(self, n: int) -> int:
        # write your code here
        hq = []
        v = set()
        heapq.heappush(hq, 1)
        v.add(1)

        for i in range(n-1):
            val = hq[0]
            val_2 = val * 2
            val_3 = val * 3
            val_5 = val * 5
            if val_2 not in v:
                v.add(val_2)
                heapq.heappush(hq, val_2)
            if val_3 not in v:
                v.add(val_3)
                heapq.heappush(hq, val_3)
            if val_5 not in v:
                v.add(val_5)
                heapq.heappush(hq, val_5)
            heapq.heappop(hq)

        return hq[0]

# sort heap
# time O(nlogn)
# space O(n)

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        # heapq is a min heap, but we need a max heap
        # so we will store negated elements
        q = []
        ptr = 0
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                # push a negated element
                heapq.heappush(q, -projects[ptr][1])
                ptr += 1
            if not q:
                break
            # pop a negated element
            w += -heapq.heappop(q)
        return w

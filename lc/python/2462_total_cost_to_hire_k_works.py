# heap
# time O((k+m)logm)
# space O(m)

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        hq = []

        for i in range(candidates):
            heapq.heappush(hq, (costs[i], 0))

        for i in range(max(candidates, n-candidates), n):
            heapq.heappush(hq, (costs[i], 1))

        ret = 0

        next_head, next_tail = candidates, n-1-candidates

        for _ in range(k):
            cur_cost, cur_section = heapq.heappop(hq)
            ret += cur_cost
            if next_head <= next_tail:
                if cur_section == 0:
                    heapq.heappush(hq, (costs[next_head], 0))
                    next_head += 1
                else:
                    heapq.heappush(hq, (costs[next_tail], 1))
                    next_tail -= 1

        return ret

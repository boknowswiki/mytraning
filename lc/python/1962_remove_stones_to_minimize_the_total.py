# heap
# time O(n+klogn)
# space O(n)
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        if not piles:
            return 0

        hq = []
        cnt = 0

        for pile in piles:
            heapq.heappush(hq, -pile)

        for _ in range(k):
            pile = -heapq.heappop(hq)
            remove = floor(pile/2)
            heapq.heappush(hq, -(pile-remove))

        #print(f"hq {hq}")
        while hq:
            cnt += -heapq.heappop(hq)

        return cnt

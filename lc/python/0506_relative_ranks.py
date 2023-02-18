# heapq
# time O(nlogn)
# space O(n)


import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        if n == 0:
            return []
        
        hq = []

        for i in range(n):
            heapq.heappush(hq, (-score[i], i))

        place = 1

        ret = [""] * n

        while len(hq) > 0:
            _, index = heapq.heappop(hq)
            if place == 1:
                ret[index] = "Gold Medal"
            elif place == 2:
                ret[index] = "Silver Medal"
            elif place == 3:
                ret[index] = "Bronze Medal"
            else:
                ret[index] = str(place)

            place += 1

        return ret

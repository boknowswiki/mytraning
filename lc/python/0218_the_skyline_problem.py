
# heap and sort
# time O(nlogn)
# space O(n)

from typing import List

import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def addsky(pos, hei):
            if sky[-1][-1] != hei:
                sky.append([pos, hei])
        
        sky = [[-1, 0]]

        positions = set([b[0] for b in buildings] + [b[1] for b in buildings])
        print(f"pos {positions}")
        live = []
        i = 0

        for t in sorted(positions):
            while i < len(buildings) and buildings[i][0] <= t:
                heapq.heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1

            while live and live[0][1] <=t :
                heapq.heappop(live)

            h = -live[0][0] if live else 0
            addsky(t, h)

        return sky[1:]

if __name__ == "__main__":
    s = Solution()
    a = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    print(s.getSkyline(a))

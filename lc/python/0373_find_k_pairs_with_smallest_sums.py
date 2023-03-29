# heap
# time O(klogk)
# space O(k)

import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = [(nums1[0]+nums2[0], nums1[0], nums2[0], 0, 0)]
        ret = []
        v = set()
        v.add((0, 0))

        while hq and len(ret) < k:
            _, n1, n2, i, j = heapq.heappop(hq)
            ret.append([n1, n2])

            if i + 1 < len(nums1) and (i+1, j) not in v:
                heapq.heappush(hq, (n2+nums1[i+1], nums1[i+1], n2, i+1, j))
                v.add((i+1, j))
            
            if j + 1 < len(nums2) and (i, j+1) not in v:
                heapq.heappush(hq, (n1+nums2[j+1], n1, nums2[j+1], i, j+1))
                v.add((i, j+1))

        return ret

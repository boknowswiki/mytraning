# sort, heap
# time O(nlogn)
# space O(n)

import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a,b in zip(nums1, nums2)]
        pairs.sort(key=lambda x: -x[1])

        top_k_hq = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_hq)
        heapq.heapify(top_k_hq)

        ret = top_k_sum * pairs[k-1][1]

        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_hq)
            top_k_sum += pairs[i][0]

            heapq.heappush(top_k_hq, pairs[i][0])

            ret = max(ret, top_k_sum*pairs[i][1])

        return ret

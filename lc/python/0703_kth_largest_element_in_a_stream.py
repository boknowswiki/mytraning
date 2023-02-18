# heapq
# time O(logn)
# space O(n)

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_hq = []
        self.max_hq = []
        for num in nums:
            heapq.heappush(self.max_hq, -num)

        while k > 0 and len(self.max_hq) > 0:
            heapq.heappush(self.min_hq, -heapq.heappop(self.max_hq))
            k -= 1

        return

    def add(self, val: int) -> int:

        heapq.heappush(self.min_hq, val)
        while len(self.min_hq) > self.k:
            heapq.heappush(self.max_hq, -heapq.heappop(self.min_hq))


        return self.min_hq[0]

      
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

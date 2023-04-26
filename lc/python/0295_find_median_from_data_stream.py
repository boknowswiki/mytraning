# heap
# time O(logn)
# space O(n)

from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
          
# heap

import heapq

class MedianFinder:

    def __init__(self):
        self.mid = None
        self.min_hq = []
        self.max_hq = []
        

    def addNum(self, num: int) -> None:
        if self.mid is None:
            self.mid = float(num)
            heapq.heappush(self.max_hq, -float(num))
            return

        if float(num) > self.mid:
            heapq.heappush(self.min_hq, float(num))
            
        else:
            heapq.heappush(self.max_hq, -float(num))

        if len(self.max_hq) > len(self.min_hq) + 1:
            heapq.heappush(self.min_hq, -heapq.heappop(self.max_hq))
        if len(self.min_hq) > len(self.max_hq):
            heapq.heappush(self.max_hq, -heapq.heappop(self.min_hq))

        if (len(self.min_hq) + len(self.max_hq)) % 2 == 0:
            self.mid = float(self.min_hq[0] -self.max_hq[0])/2.0
        else:
            self.mid = -self.max_hq[0]
            
        return

    def findMedian(self) -> float:
        return self.mid


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinder:

    def __init__(self):
        self.mid = None
        self.min_hq = []
        self.max_hq = []
        

    def addNum(self, num: int) -> None:
        if self.mid is None:
            self.mid = float(num)
            heapq.heappush(self.max_hq, -float(num))
            return
        
        if float(num) > self.mid:
            heapq.heappush(self.min_hq, float(num))
        else:
            heapq.heappush(self.max_hq, -float(num))
            
        if len(self.max_hq) > len(self.min_hq)+1:
            heapq.heappush(self.min_hq, -heapq.heappop(self.max_hq))
        if len(self.max_hq) < len(self.min_hq):
            heapq.heappush(self.max_hq, -heapq.heappop(self.min_hq))
            
        #print(f"add {num}, {self.max_hq}, {len(self.max_hq)}, {self.min_hq}, {len(self.min_hq)}")
        if (len(self.max_hq) + len(self.min_hq)) % 2 == 0:
            #print("need divid")
            val_1 = self.max_hq[0]
            val_2 = self.min_hq[0]
            #print(f"max 0 {val_1}, min 0 {val_2}")
            self.mid = float(-float(self.max_hq[0]) + float(self.min_hq[0]))/2.0
        else:
            #print("no divid")
            self.mid = -self.max_hq[0]
            
        #print(f"mid {self.mid}")
        return
        

    def findMedian(self) -> float:
        return self.mid

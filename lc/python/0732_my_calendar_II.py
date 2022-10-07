
# sweep line

# Let N be the number of events booked.

# Time Complexity: O(N^2). For each new event, we update the changes at two points in O(\log{N})O(logN) because we keep the HashMap in sorted order. Then we traverse book_hist
# in O(N) time.

# Space Complexity: O(N), the size of book_hist.

from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.book_hist = SortedDict()
        

    def book(self, start: int, end: int) -> int:
        self.book_hist[start] = self.book_hist.get(start, 0) + 1
        self.book_hist[end] = self.book_hist.get(end, 0) - 1
        cur = ret = 0
        for val in self.book_hist.values():
            cur += val
            ret = max(ret, cur)
            
        return ret
      
# segment tree
    
#Let N be the number of events booked and C be the largest time (i.e., 10^9 in this problem)

# Time Complexity: O(NlogC). The max possible depth of the segment tree is logC. At most O(logC) nodes will be visited in each update operation. Thus, the time complexity of booking N new events is O(NlogC).
# Space Complexity: O(NlogC). Instead of creating a segment tree of 4C at first, we create tree nodes dynamically when needed. Every time update is called, we create at most O(logC) nodes because the max depth of the segment tree is logC
    
from collections import Counter

class MyCalendarThree:

    def __init__(self):
        self.vals = Counter()
        self.lazy = Counter()
        

    def book(self, start: int, end: int) -> int:
        self.update(start, end-1)
        return self.vals[1]
    
    def update(self, start: int, end: int, left: int = 0, right: int = 10**9, index: int= 1) -> None:
        if start > right or end < left:
            return
        
        if start <= left <= right <= end:
            self.vals[index] += 1
            self.lazy[index] += 1
        else:
            mid = left + (right-left)//2
            self.update(start, end, left, mid, index*2)
            self.update(start, end, mid+1, right, index*2+1)
            self.vals[index] = self.lazy[index] + max(self.vals[2*index], self.vals[2*index+1])
        

        

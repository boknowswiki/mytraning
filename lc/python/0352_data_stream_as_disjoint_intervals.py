# binary search
# time O(logn)
# space O(n)


class SummaryRanges:

    def __init__(self):
        self.intervals = []
        

    def addNum(self, value: int) -> None:
        # find location
        #print(f"add value {value}, intervals {self.intervals}")
        if len(self.intervals) == 0:
            self.intervals = [[value, value]]
            return
        low, high = 0, len(self.intervals) - 1
        while low <= high:
            mid = (low + high) // 2
            elem = self.intervals[mid]
            if elem[0] <= value <= elem[1]:
                return
            elif elem[0] > value:
                high = mid - 1
            else:
                low = mid + 1

        # insert the interval
        pos = min(low, high) + 1
        self.intervals[pos:pos] = [[value, value]]
        #print(f"pos {pos}, intervals {self.intervals}")

        # merge with next interval
        if pos + 1 < len(self.intervals) and value == self.intervals[pos + 1][0] - 1:
            self.intervals[pos][1] = self.intervals[pos + 1][1]
            self.intervals[pos + 1:pos + 2] = []
            #print(f"after merge with next intervals {self.intervals}")

        # merge with prev interval
        if pos - 1 >= 0 and value == self.intervals[pos - 1][1] + 1:
            self.intervals[pos - 1][1] = self.intervals[pos][1]
            self.intervals[pos:pos + 1] = []     
            #print(f"after merge with prev intervals {self.intervals}")
        

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
        

        
class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        seen = set()
        for num in self.nums:
            if num in seen: 
                continue

            left = num
            while left - 1 in self.nums:
                left -= 1
                seen.add(left)

            right = num
            while right + 1 in self.nums:
                right += 1
                seen.add(right)
            
            intervals.append([left, right])
        return sorted(intervals)

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

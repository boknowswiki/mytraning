#!/usr/bin/python -t

#用扫描线，python bisect 不支持tuple, 用两个数组：
#attr : X (start or end value)
#count: 1 or -1 (correpeonding to attr array element is start or end)


import bisect

class MyCalendarTwo(object):

    def __init__(self):
        self.mapping = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        bisect.insort(self.mapping, [start, 1])
        bisect.insort(self.mapping, [end, -1])
        
        cnt = 0
        for i in range(len(self.mapping)):
            cnt += self.mapping[i][1]
            if cnt == 3:
                self.mapping.pop(bisect.bisect_left(self.mapping, [start, 1]))
                self.mapping.pop(bisect.bisect_left(self.mapping, [end, -1]))
                return False
                
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


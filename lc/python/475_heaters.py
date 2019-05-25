#!/usr/bin/python -t 

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i+2]) / 2.:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        def binarysearch(a, i):
            """
            e.g. a = [10, 20, 30, 40]
            print(Solution().bSearchNearest(a, 9)) <- 0
            print(Solution().bSearchNearest(a, 10)) <- 0
            print(Solution().bSearchNearest(a, 13)) <- 0
            print(Solution().bSearchNearest(a, 21)) <- 1
            print(Solution().bSearchNearest(a, 26)) <- 2
            print(Solution().bSearchNearest(a, 34)) <- 2
            print(Solution().bSearchNearest(a, 35)) <- 3
            print(Solution().bSearchNearest(a, 41)) <- 3
            """
            l = 0
            r = len(a) - 1
        
            while l < r:
                m = l + (r-l)/2
            
                if a[m] == i:
                    return m
                elif a[m] < i:
                    l = m + 1
                else:
                    r = m
                
                if l > 0 and abs(i - a[l-1]) < abs(i- a[l]):
                    return l-1
                
            return l
        
        heaters.sort()
        ret = 0
        for i in houses:
            index = binarysearch(heaters, i)
            print index
            diff = abs(i - heaters[index])
            ret = max(ret, diff)
            
        return ret

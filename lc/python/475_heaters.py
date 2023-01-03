#!/usr/bin/python -t 

# sort and two pointers

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.extend([float('-inf'), float('inf')])
        heaters.sort()
        
        radius = 0
        i = 1
        
        for house in houses:
            while heaters[i] < house: i += 1
            min_dist = min(house-heaters[i-1], heaters[i]-house)
            radius = max(radius, min_dist)
            
        return radius

# binary search
# time O(nlogn)
# space O(1)

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ret = 0
        
        for house in houses:
            index = self.find_lower(heaters, house)
            diff = abs(house-heaters[index])
            ret = max(ret, diff)
            
        return ret
    
    def find_lower(self, arr, target):
        l = 0
        r = len(arr)-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid
            else:
                r = mid
                
        if abs(target-arr[r]) < abs(target-arr[l]):
            return r
        return l
            

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

#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        heaters.sort()
        ans = 0
        for house in houses:
            ans=max(ans,self.closestHeater(house,heaters))
        return ans
        
    def closestHeater(self,house,heaters):
        start = 0
        end = len(heaters) - 1
        while start < end:
            m = start + (end - start) // 2
            if heaters[m] == house:
                return 0
            elif heaters[m] < house:
                start = m+1
            else:
                end = m
                
        return min(abs(house - heaters[start]), abs(heaters[end-1] - house))


# binary search solution

class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        heaters.sort()
        ans = 0
        for house in houses:
            ans=max(ans,self.closestHeater(house,heaters))
        return ans
        
    def closestHeater(self,house,heaters):
        start = 0
        end = len(heaters) - 1
        while start +1 < end:
            m = start + (end - start) // 2
            if heaters[m] == house:
                return 0
            elif heaters[m] < house:
                start = m
            else:
                end = m
                
        return min(abs(house - heaters[start]), abs(heaters[end] - house))


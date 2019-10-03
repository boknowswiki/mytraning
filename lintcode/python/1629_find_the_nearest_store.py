#!/usr/bin/python -t

# binary search

class Solution:
    """
    @param stores: The location of each store.
    @param houses: The location of each house.
    @return: The location of the nearest store to each house.
    """
    def findNearestStore(self, stores, houses):
        # 
        stores.sort()
        ret = []
        if not stores:
            return ret
            
        for h in houses:
            ret.append(self.lower_bound(stores, h))
            
        return ret
        
    def lower_bound(self, stores, h):
        l = 0
        r = len(stores)-1
        
        while l < r:
            mid = (l+r)/2
            if stores[mid] == h:
                return stores[mid]
            elif stores[mid] < h:
                l = mid+1
            else:
                r = mid
                
        if abs(stores[l]-h) < abs(stores[l-1]-h):
            return stores[l]
        else:
            return stores[l-1]

if __name__ == '__main__':
    s = [1,3,6]
    v = [2,4,6,7]
    ss = Solution()
    print "answer is\n"
    print ss.findNearestStore(s, v)

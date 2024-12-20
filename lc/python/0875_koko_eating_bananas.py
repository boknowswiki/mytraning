
# binary search
# time O(nlogn)
# space O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time(val):
            t = 0

            for p in piles:
                t += p // val

                if p % val:
                    t += 1

            return t
                
        l = 1
        r = max(piles)

        while l + 1 < r:
            mid = (l+r)//2
            t = get_time(mid)
            if t > h:
                l = mid+1
            else:
                r = mid

        if get_time(l) <= h:
            return l
        return r

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        while l + 1 < r:
            mid = l + (r-l)//2
            print(f"l {l}, r {r}, mid {mid}")
            time = self.get_time(piles, mid)
            print(f"time {time}")
            if time > h:
                l = mid
            else:
                r = mid
                
        if self.get_time(piles, l) <= h:
            return l
        if self.get_time(piles, r) <= h:
            return r
        
        return -1
    
    def get_time(self, piles, target):
        time = 0
        
        for p in piles:
            if p%target != 0:
                time += p//target + 1
            else:
                time += p//target
                
        return time

if __name__ == "__main__":
    s = Solution()
    a = [3,6,7,11]
    b = 8
    print(s.minEatingSpeed(a,b))

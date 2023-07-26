# binary search
# time O(nlogk)
# space O(1)

import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        l = 1
        r = 10000000

        def get_hours(speed):
            need_hour = 0

            for i in range(n):
                if i != n-1:
                    need_hour += math.ceil(dist[i]*1.0/speed)
                else:
                    need_hour += dist[i]*1.0/float(speed)

            return need_hour

        ret = -1

        while l <= r:
            mid = (l+r)//2
            need = get_hours(mid)
            if need <= hour:
                ret = mid
                r = mid-1
            else:
                l = mid+1

        return ret

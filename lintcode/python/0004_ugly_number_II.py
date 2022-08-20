#!/usr/bin/python -t

# heap
# time O(nlogn)
# space O(n)


import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nth_ugly_number(self, n: int) -> int:
        # write your code here
        hq = []
        v = set()
        heapq.heappush(hq, 1)
        v.add(1)

        for i in range(n-1):
            val = hq[0]
            val_2 = val * 2
            val_3 = val * 3
            val_5 = val * 5
            if val_2 not in v:
                v.add(val_2)
                heapq.heappush(hq, val_2)
            if val_3 not in v:
                v.add(val_3)
                heapq.heappush(hq, val_3)
            if val_5 not in v:
                v.add(val_5)
                heapq.heappush(hq, val_5)
            heapq.heappop(hq)

        return hq[0]


# better one
# time O(n)

class Solution {
    public int nthUglyNumber(int n) {
        int[] res = new int[n];
        res[0] = 1;
        int p2 = 0;
        int p3 = 0;
        int p5 = 0;
        
        for (int i = 1; i < n; i++) {
            res[i] = Math.min(res[p2] * 2, Math.min(res[p3] * 3, res[p5] * 5) );
            if (res[i] == res[p2] * 2) {
                p2++;
            }
            if (res[i] == res[p3] * 3) {
                p3++;
            }
            if (res[i] == res[p5] * 5) {
                p5++;
            }
        }
        return res[n - 1];
        
    }
}

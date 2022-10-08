# binary search and sort
# time O(nlogn)
# space O(n)

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        #print(envelopes)
        LIS = []
        size = 0
        for (w, h) in envelopes:
            if not LIS or h > LIS[-1]:
                LIS.append(h)
                size += 1
            else:
                l, r = 0, size
                while l+1 < r:
                    m = l + (r - l) // 2
                    if LIS[m] <= h:
                        l = m
                    else:
                        r = m
                if h > LIS[l]:
                    LIS[r] = h
                else:
                    LIS[l] = h
        return len(LIS)

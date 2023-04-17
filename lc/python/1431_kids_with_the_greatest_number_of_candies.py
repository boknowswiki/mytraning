# array
# time O(n)
# space O(1)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        n = len(candies)
        if n == 0:
            return ret

        max_val = max(candies)

        for i in range(n):
            if candies[i] + extraCandies >= max_val:
                ret.append(True)
            else:
                ret.append(False)

        return ret

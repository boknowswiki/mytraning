# sort
# time O(nlogn)
# space O(1)

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not coins or not costs:
            return 0

        costs.sort()
        total = 0
        ret = 0

        for cost in costs:
            total += cost
            if total <= coins:
                ret += 1
            else:
                break

        return ret

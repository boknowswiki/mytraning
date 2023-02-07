# hash map and sliding window
# time O(n)
# space O(1)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n < 3:
            return n

        basket = dict()
        ret = 0
        l = 0
        for r in range(n):
            basket[fruits[r]] = basket.get(fruits[r], 0)+1
            while l < r and len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1

            ret = max(ret, r-l+1)

        return ret

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n < 3:
            return n

        basket = dict()
        ret = 0
        l = 0
        for r in range(n):
            basket[fruits[r]] = basket.get(fruits[r], 0)+1
            while l < r and len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1

            ret = max(ret, sum([v for _, v in basket.items()]))

        return ret

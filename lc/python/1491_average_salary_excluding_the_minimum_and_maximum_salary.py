# array, sort
# time O(n)
# space O(1)

class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        if n < 3:
            return 0
        min_val = salary[0]
        max_val = salary[0]
        total = 0

        for s in salary:
            total += s
            if s < min_val:
                min_val = s
            if s > max_val:
                max_val = s

        total -= min_val
        total -= max_val

        return total/(n-2)

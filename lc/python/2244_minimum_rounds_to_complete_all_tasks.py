# greedy and count and hash map
# time O(n)
# space O(n)

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = dict()

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        ret = 0

        for cnt in counts.values():
            if cnt == 1:
                return -1

            if cnt % 3 == 0:
                ret += cnt//3
            else:
                ret += cnt//3 + 1

        return ret

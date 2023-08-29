# string, prefix sum
# time O(n)
# space O(1)

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur_penalty = min_penalty = customers.count("Y")
        earliest_hour = 0

        for i, state in enumerate(customers):
            if state == "Y":
                cur_penalty -= 1
            else:
                cur_penalty += 1

            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                earliest_hour = i+1

        return earliest_hour

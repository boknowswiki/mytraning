#!/usr/bin/python -t

# stack
# time O(n)
# space O(n)

from typing import (
    List,
)

class Solution:
    """
    @param n: a integer
    @param logs: a list of strings
    @return: return a list of integers
    """
    def exclusive_time(self, n: int, logs: List[str]) -> List[int]:
        # write your code here
        ret = [0 for _ in range(n)]
        stack = []
        last_timestamp = 0

        for line in logs:
            log = line.split(":")
            func_id, status, timestamp = int(log[0]), log[1], int(log[2])

            if status == "start":
                if stack:
                    ret[stack[-1]] += timestamp - last_timestamp
                stack.append(func_id)
            else:
                timestamp += 1
                ret[stack[-1]] += timestamp - last_timestamp
                stack.pop()
            last_timestamp = timestamp

        return ret

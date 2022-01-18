#!/usr/bin/python -t

class Solution:
    """
    @param n: The number of tasks
    @param t: The time array t
    @param p: The probability array p
    @return: Return the order
    """
    def getOrder(self, n, t, p):
        # Write your code here
        tasks = []
        for i in range(n):
          priority = round(p[i]/t[i],5)
          tasks.append((-priority, i))

        tasks.sort()
        return [task[1]+1 for task in tasks]

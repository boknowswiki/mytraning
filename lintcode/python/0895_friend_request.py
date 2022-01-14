#!/usr/bin/python -t

class Solution:
    """
    @param ages: The ages
    @return: The answer
    """
    def friendRequest(self, ages):
        # Write your code here
        ans = 0
        for i in range(0, len(ages)):
            for j in range(0, len(ages)):
                if (i == j):
                    continue
                A = ages[i]
                B = ages[j]
                if(B <= A and B > A // 2 + 7 and not (B < 100 and A > 100)):
                    ans += 1
        return ans

#!/usr/bin/python -t

# prefix sum

class Solution:
    """
    @param a: the list of salary
    @param target: the target of the sum
    @return: the cap it should be
    """
    def getCap(self, a, target):
        # Write your code here.
        n = len(a)
        a.sort()
        pre_sum = 0
        for i in range(n-1, -1, -1):
            need = (target-pre_sum)/(i+1)
            if need >= a[i]:
                return need+1 if (target-pre_sum)%(i+1) else need
            pre_sum += a[i]
            
        return -1


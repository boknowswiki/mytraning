#!/usr/bin/python -t


# 对于有四个人的小组，必须单独一辆车。
# 
# 随后对于三个人的小组，优先安排与只有一个人的小组拼车，剩下的三人小组每个组单独一辆车
# 
# 随后对于两人小组，优先安排与其他两人小组拼车，如果存在落单的两人小组，则优先与两个一人小组拼车。
# 
# 对于最后剩下的一人小组，优先安排四个小组一辆车，如果有剩下的则单独一辆车。

class Solution:
    """
    @param a: The array a
    @return: Return the minimum number of car
    """
    def getAnswer(self, a):
        # Write your code here
        count = [0 for i in range(0, 5)]
        for i in range(0, len(a)):
        	count[a[i]] = count[a[i]] + 1
        count[1] = count[1] - count[3]
        if count[2] % 2 == 1:
        	count[2] = count[2] + 1
        	count[1] = count[1] - 2
        res = count[4] + count[3] + count[2] / 2
        if count[1] > 0:
        	res = res + count[1] / 4
        	if not count[1] % 4 == 0:
        		res = res + 1
        return int(res)

#!/usr/bin/python -t

# sort

class Solution:
    """
    @param lunch: an array that contains each lunch food's calories and value
    @param dinner: an array that contains each dinner food's calories and value
    @param T: the minest limit value
    @return: return the min calories
    """
    def getMinCalories(self, lunch, dinner, T):
        # write your code here

        # 按照美味程度排序，排序之后可以双指针
        lunch.sort(key=lambda x: x[1])
        dinner.sort(key=lambda x: x[1])
        
        # lunch 和 dinner 必须每种都选
        ret = float('inf')
        j = len(dinner)-1
        
        min_energy_dinner = float('inf')
        for i in range(len(lunch)):
            while j >= 0 and lunch[i][1] + dinner[j][1] >= T:
                min_energy_dinner = min(min_energy_dinner, dinner[j][0])
                j-=1
            ret = min(ret, lunch[i][0] + min_energy_dinner)
        
        # 只选择 lunch 或者 dinner
        for energy, taste in lunch + dinner:
            if taste >= T and energy < ret:
                ret = energy

        return -1 if ret == float('inf') else ret

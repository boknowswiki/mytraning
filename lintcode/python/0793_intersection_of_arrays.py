
# hash

class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        count = {}
        # 记录每个数的出现次数
        for arr in arrs:
            for x in arr:
                if x not in count:
                    count[x] = 0
                count[x] += 1
        
        # 某个数出现次数等于数组个数，代表它在所有数组中都出现过
        result = 0
        for x in count.keys():
            if count[x] == len(arrs):
                result += 1
        return result

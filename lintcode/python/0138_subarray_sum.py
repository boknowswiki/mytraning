#!/usr/bin/python -t

# hash table

#使用prefix_sum进行求解
#根据随课教程中对于prefix_sum的定义：
#prefix_sum[i] = nums[0] + nums[1] + .. + nums[i - 1] and prefix_sum[0] = 0
#sum([i, j]) = prefix_sum[j + 1] - prefix_sum[i] (注意[i, j]是一个包含i, j的闭区间)
#根据令狐老师的点拨,
#和为0的[i, j]闭区间
#<=> sum([i, j]) = 0
#<=> prefix_sum[j + 1] - prefix_sum[i] = 0
#<=> prefix_sum[j + 1] = prefix_sum[i]


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        sum = 0
        nums.insert(0,0)
        d = dict()
        for i in range(len(nums)):
            sum += nums[i]
            if sum in d:
                return [d[sum],i-1]
            else:
                d[sum] = i
        

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        nums.insert(0, 0)
        n = len(nums)
        sum_val = 0
        record = {}
        ret = []
        
        for i in range(n):
            sum_val += nums[i]
            print sum_val
            
            if sum_val in record:
                l = record[sum_val]
                ret.append([l, i-1])
                
            record[sum_val] = i
            
        return ret


# myself solution

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return [-1, -1]
            
        total = 0
        d = {0: -1}
        
        for i in range(n):
            total += nums[i]
            #print total, nums[i]
            if total in d:
                #print "got it"
                #print d, total, i
                ret = [d[total]+1, i]
                return ret
                
            d[total] = i
            #print d
                
        return [-1, -1]
        
                
        
        

if __name__ == '__main__':
    s = [-4,1,2,-3,4]


    ss = Solution()
    print "answer is %s" % ss.subarraySum(s)


#!/usr/bin/python -t

# binary search
#使用九章算法强化班中讲过的基于二分答案的方法
#二分出 average 之后，把数组中的每个数都减去 average，然后的任务就是去求这个数组中，是否有长度 >= k 的 subarray，他的和超过 0。
#这一步用类似 Maximum Subarray 的解法来做就好了

class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        csum = [0]
        for i in range(len(nums)):
            csum.append(csum[i]+nums[i])

        print csum
        res = float(csum[k])/k
        check = 0
        for i in range(k+1,len(csum)):
            left = float((csum[i] - csum[check]))/(i - check)
            right = float((csum[i] - csum[i-k]))/k
            print i, check, left, right
            if left >= right:
                if left > res:
                    res = left
            else:
                if right > res:
                    res = right
                check = i - k
        return res

if __name__ == '__main__':
    s = [-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000]
    t = 10
    ss = Solution()
    print "answer is\n"
    print ss.maxAverage(s, t)

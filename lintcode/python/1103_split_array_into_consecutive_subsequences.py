#!/usr/bin/python -t

# hash table

# 首先统计好每个数字出现的次数
# 
# 从最小的数字开始, 假设当前数字为num
# 
# 先看看有没有数组以num - 1结尾, 有的话直接把num放过去, 然后以num - 1结尾的数组个数减1, 以num为结尾的数组的个数加1, num的频率减1, 继续下一个数字
# 如果以num - 1结尾的数组个数不够了, 说明需要建立新的数组, 就要看num + 1和num + 2是否还有, 有的话就建立新的数组, 此时多了一个以num + 2结尾的数组, 所以num + 2结尾的数组个数加1, 同时num + 1, num + 2的频率减1, 最后num的频率也减1, 继续...
# 以上两点都不满足的话, 说明当前数字放不到任意一个已有的数组末尾, 并且也不能建立新的长度大于等于3的数组了, 返回False
# 时间: O(n)
# 空间: O(n)


class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def isPossible(self, nums):
        # write your code here
        freq = {}
        tail = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            tail[num] = 0
            
        for num in nums:
            if freq[num] == 0:
                continue
            if num-1 in tail and tail[num-1] > 0:
                tail[num-1] -=1
                tail[num] += 1
            elif num+1 in tail and num+2 in tail and freq[num+1] > 0 and freq[num+2]>0:
                tail[num+2] += 1
                freq[num+1] -= 1
                freq[num+2] -= 1
            else:
                return False
                
            freq[num] -= 1
            
        return True
        

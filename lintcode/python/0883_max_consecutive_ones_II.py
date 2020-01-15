#!/usr/bin/python -t

# two pointers
#首先考虑Corner case
#
#然后设置start end 指针，上一个0的位置指针， 以及此时0的数量
#
#遍历数组
#
#如果此时遇到0， 先判断是第几个0，如果是第二个0，那就把此时的新起点设置在上一个0位置+1, 同时0的数目归1
#遇到第一个0的话就把0数目增加即可。
#两种情况都要刷新此时的上一个0的位置
#
#如果不是0，就正常进行
#每次循环结束前更新此时遍历的位置为end，并统计长度，不断对比
#
#最后得到最长的长度

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        n = len(nums)
        start = 0
        end = 0
        cnt_z = 0
        prev_z = 0
        ret = 0
        
        for i in range(n):
            if nums[i] == 0:
                cnt_z += 1
                if cnt_z > 1:
                    start = prev_z + 1
                    cnt_z = 1
                prev_z = i
                
            end = i
            ret = max(ret, end-start+1)
            
        return ret
        

# dp
#Dp[i][0] 表示以第i个位置为结尾，没有反转过，最长的长度。
#Dp[i][1] 表示以第i个位置为结尾，最多反转过1次的最长的长度。
#
#分当前是0 还是1，两种状态分别转移。（可以知道的是，每次Dp[i][1]>=Dp[i][0]）
#
#空间可以优化到O(1)

/**
* This reference program is provided by @jiuzhang.com
* Copyright is reserved. Please indicate the source for forwarding
*/

public class Solution {
    /**
     * @param nums: a list of integer
     * @return: return a integer, denote  the maximum number of consecutive 1s
     */
    public int findMaxConsecutiveOnes(int[] nums) {
        // write your code here
        int n = nums.length;
        int[][] Dp = new int[10005][2];
        if(nums[0] == 1) {
            Dp[0][0] = 1;
            Dp[0][1] = 1;
        } else {
            Dp[0][1] = 1;
            Dp[0][0] = 0;
        }
        int Max = 1;
        for(int i = 1; i < n; i++) {
            if(nums[i] == 0) {
                Dp[i][1] = 1 + Dp[i-1][0];
                Dp[i][0] = 0;
            } else {
                Dp[i][0] = 1 + Dp[i-1][0];
                Dp[i][1] = 1 + Dp[i-1][1];
            }
            Max = Math.max(Max, Dp[i][1]);
        }
        return Max;
    }
}

# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        can_still_flip, no_more_flips, max_ones = 0, 0, 0
        
        for num in nums:
            
            if num == 1:
                can_still_flip += 1 
                no_more_flips += 1
            else:
                can_still_flip += 1 
                no_more_flips, can_still_flip = can_still_flip, 0
                
            max_ones = max(max_ones, can_still_flip, no_more_flips)

        return max_ones

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        ret = 0
        flip = 0
        no_flip = 0
        
        for num in nums:
            if num == 0:
                flip += 1
                flip, no_flip = 0, flip
                
            else:
                flip += 1
                no_flip += 1
            
            ret = max(ret, flip, no_flip)
            
        return ret
        
        

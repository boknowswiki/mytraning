#!/usr/bin/python -t

#one[i] means the min flip number we need for preious i number in nums when the last number in the previous i numbers is 1;
#
#zero[i] means the min flip number we need for previous i numbers in nums when last number in previous i numbers is 0;
#
#zero[0] = 0; one[0] = 0;
#
#in the for loop, we will update one and zero from 1 to nums.length; i in zero and one mean the number of previous numbers.
#
#therefore we will have two different cases depending on whether nums[i - 1] is 1 or 0;
#
#if nums[i - 1] is 1,
#one[i] dont need to flip the last digit, since only 1 can be before 1, so one[i] = one[i - 1];
#however, zero[i] need to flip the last digit, +1, if last one is 0, we can set its previous one as 1 or 0; zero[i] = 1 + Math.min(one[i - 1], zero[i - 1]);
#
#if nums[i - 1] is 0,
#one[i] needs to flip the last digit, +1, only 1 can be before 1. so one[i] = one[i - 1] + 1;
#zero[i] dont need to flip, 1 or 0 both can be before 0. zero[i] = Math.min(zero[i-1], one[i - 1]);

class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        # Write your code here
        n = len(nums)
        
        zero = [0] * (n+1)
        one = [0] * (n+1)
        
        for i in range(1, n+1):
            zero[i] = min(zero[i-1], one[i-1]) if nums[i-1] == 0 else min(zero[i-1], one[i-1])+1
            one[i] = one[i-1] if nums[i-1] == 1 else one[i-1]+1

        print zero, one
            
        return min(zero[n], one[n])

if __name__ == '__main__':
    s = [1,0,0,1,1,1]
    ss = Solution()
    print "answer is %s" % ss.flipDigit(s)

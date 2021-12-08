#!/usr/bin/python -t

# string
# 考点：
# 
# 贪心
# 数学
# 题解：只需要证明，对于任何 > 或者 < , 算法的规则都能满足。
# △N = max-min; 由于每次遇到一个符号，△N-1。
# 当符号为“ <   <   <”: max--可以保证符号的正确性。
# 当符号为“ >   >   >”: min++可以保住符号的正确性。
# 当符号为“ ……<   >   < ":  任意时刻max和min开始比较，是否满足 min < max?
# 由于符号的数量为N，最开始△N = N。由于至少出现一对大于号和小于号 , min(△N)= 1，仍然满足min < max。
# 因为每一位对应的数字只有两种情况：比右边所有数都大，或者都小。那么我们可以设定两个值，初始的话：low = 0，high = N。这样，从左开始遍历字符串，碰见一个字符，如果是‘I’，那么就直接赋值low，同时low++。这样，‘I’右边所有的数，一定是都比这个位置大的。因为此时low>a[i]，同时high > low。
# 反而言之，碰见‘D’，直接赋值hight，同时high--。这样所有的数就一定比这个小了。大概就是这样，在O(n)的时间复杂度下就能构造出答案数组。
# 
class Solution:
    def diStringMatch(self, S):
        n = len(S)
        nums = [i for i in range(n+1)]
        l = 0
        r = n
        ret = []
        for i in range(n):
            if S[i] == 'I':
                ret.append(nums[l])
                l+=1
            else:
                ret.append(nums[r])
                r -= 1

        ret.append(nums[l])

        return ret

if __name__ == '__main__':
    s = Solution()
    a = "IDID"
    print(s.diStringMatch(a))
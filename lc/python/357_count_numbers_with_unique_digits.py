#!/usr/bin/python -t

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(target, index, visit):
            if index == target:
                return 1
            cnt = 0
            
            for i in range(0 if index else 1, 10, 1):
                if not visit[i]:
                    visit[i] = True
                    cnt += dfs(target, index+1, visit)
                    visit[i] = False
                    
            return cnt
            
        visit = [False] * 10
        cnt = 0
        for i in range(min(10, n)+1):
            cnt += dfs(i, 0, visit)
            
        return cnt

'''
#java solution

class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            int product = 9;
            for (int j = 0; j < i - 1; j++) {
                product *= (9 - j);
            }
            dp[i] = dp[i - 1] + product;
        }
        return dp[n];
    }
}

#when n is 0, it is clear that there is just one number 0.
#when n is 1, it is trivial that there are 10 numbers: 0,1,2...9.
#when n is 2, the range is [0, 99]. The total unique digits is divided to two part: just one digit or two digit.
#          **dp[2]  = dp[1] + the combination with  two digits.** 
#'0' could only be at unit digit. so when '0' is at unit digit, there are 9 kinds of. when there is no '0', there are 9 kinds of numbers at tens digit, and 8 kinds of numbers at unit digit. So the combination with two digits are: 9 + 9*8 is equal to
#                                   9 * (1+8) = 9 * 9.
#when n is 3, the range is [0, 999]. The total unique digits is divided to two part: less than 3 digit or 3 digit.
#          **dp[3]  = dp[2] + the combination with  3 digits.** 
#'0' could only be at unit digit and ten's digit.
#When '0' is at unit digit, there are 9 * 8 kind of numbers(9 is the kind of numbers at hundred's digit, 8 is the kind of numbers at ten's digit);
#When '0' is at ten's digit, there are 9 * 8 kind of numbers(9 is the kind of numbers at hundred's digit, 8 is the kind of numbers at unit digit);
#When there is no '0', there are 9 * 8 * 7 kinds of numbers(9 is the kind of numbers at hundred's digit, 8 is the kind of numbers at ten's digit, 7 is the kind of numbers at unit digit).
#So there are:
#             9 * 8  + 9 * 8 + 9 * 8 * 7  = 9 * 8 * (1 + 1 + 8 ) = 9 * 9 * 8 
#kinds of combinations with three digits.
#.........
#Than it is easy to understand the DP solution of this problem.

#time O(n) space O(n)

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        
        l = [0]*(n+1)
        l[0] = 1
        l[1] = 10
        
        for i in range(2, n+1):
            l[i] = 9
            j = 9
            cnt = 1
            
            while cnt < i:
                l[i] *= j
                j -= 1
                cnt += 1
                
            l[i] += l[i-1]
            
        return l[n]

#This is a digit combination problem. Can be solved in at most 10 loops.
#When n == 0, return 1. I got this answer from the test case.
#When n == 1, _ can put 10 digit in the only position. [0, ... , 10]. Answer is 10.
#When n == 2, _ _ first digit has 9 choices [1, ..., 9], second one has 9 choices excluding the already chosen one. So totally 9 * 9 = 81. answer should be 10 + 81 = 91
#When n == 3, _ _ _ total choice is 9 * 9 * 8 = 684. answer is 10 + 81 + 648 = 739
#When n == 4, _ _ _ _ total choice is 9 * 9 * 8 * 7.
#...
#When n == 10, _ _ _ _ _ _ _ _ _ _ total choice is 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
#When n == 11, _ _ _ _ _ _ _ _ _ _ _ total choice is 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 * 0 = 0

#time O(n) space O(1)

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        
        op = 9
        pro = 9
        ret = 10
        
        for i in range(1, n if n <= 10 else 10):
            pro *= op
            ret += pro
            op -=1
            
        return ret
'''
if __name__ =='__main__':
    ss = Solution()
    print('answer is %d' % ss.countNumbersWithUniqueDigits(2))


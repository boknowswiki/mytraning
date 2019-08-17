#!/usr/bin/python -t

'''
#先解释为什么10层楼的时候用4次
#先从floor4扔
#break了，就需要用另一个从floor1开始往上找，最多用3次，一共4次
#没有break，再从floor7扔
#break了，就需要用另一个从floor5开始往上找，最多用2次，一共是4次
#没有break， 再从floor9扔
#break了，就需要用另一个从floor8开始往上找，最多用1次，一共是4次
#没有break，确定是 k = 10
#倒过来看就是一个等差数列的过程：[10], [9, 8], [7, 6, 5], [4, 3, 2, 1]
#所以累加的方法就是找到最小的m，使得1到m的公差为1的等差数列的和大于n
#
#然后直接求解就是，等差数列的和为 m * (m + 1) / 2,
#令其大于等于 n，
#得到 m ** 2 + m - 2n >= 0,
#然后用一元二次方程求解公式取正值，
#再取ceil()就可以了
'''

class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        # write your code here
        res = 1
        sum = 1
        while sum < n:
            res += 1
            sum += res
        return res

if __name__ == '__main__':
    s = 10
    ss = Solution()
    print "answer is %s" % ss.dropEggs(s)


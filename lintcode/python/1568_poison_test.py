#!/usr/bin/python -t

# binary

# 所需要的小白鼠的数量M为最小的满足2^M >= n的M
# 为什么这样是对的呢？
# 首先我们将每瓶水按顺序用格雷码进行编号（例如0000,0001,0010,0011,0100....）
# （你可以把此处的格雷码理解成第i个(2<=i<=n)二进制编号和第i-1个二进制编号仅有一位不同）
# 编号的第i位代表第i只小白鼠是(1)否(0)喝的东西里是否含有这瓶水的成分（例如01101代表1,3,4号小白鼠喝了这种水），并且算出至少多少位二进制能够将所有的小白鼠进行完全编号（M）
# 在试验结束后小白鼠的存活状态我们也用一个01串来表示，0表示没死，1表示死了，那么我们编号与这个01串相同的水就是毒药
# （因为喝了这瓶水的小白鼠都死了）
class Solution:
    """
    @param n: There are n bottles of water
    @return: Return the number of mice
    """
    def getAns(self, n):
        # Write your code here
        num = 1
        cnt = 0
        while num < n:
            num *= 2
            cnt += 1

        return cnt


if __name__ == '__main__':
    s = Solution()
    a = 8
    print(s.getAns(a))
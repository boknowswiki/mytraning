#!/usr/bin/python -t


# dfs

from typing import (
    List,
)

class Solution:
    def __init__(self):
        self.cur_max = 0
        self.ret = None
    """
    @param score: When the j-th driver gets the i-th order, we can get score[i][j] points.
    @return: return an array that means the array[i]-th driver gets the i-th order.
    """
    def orderAllocation(self, score: List[List[int]]) -> List[int]:
        # write your code here
        m = len(score)
        ret = [None] * m

        self.dfs(score, 0, ret)

        return self.ret

    def dfs(self, score, index, ret):
        print(score, index, ret)
        if index == len(ret):
            val = 0
            for i in range(len(ret)):
                val += score[i][ret[i]]

            if val > self.cur_max:
                self.cur_max = val
                self.ret = list(ret)
            return

        for i in range(len(ret)):
            if i not in ret:
                ret[index] = i
                self.dfs(score, index+1, ret)
                ret[index] = None
        
        return

if __name__ == '__main__':
    s = Solution()
    a = [[1,2,4],[7,11,16],[37,29,22]]

    print(s.orderAllocation(a))


# dp

# 状态压缩DP版
# 我硬生生把一个medium题目做成了Hard。 不过你们也可以看一眼， 能练习状态压缩的题目真的不多了。
# 
# 首先这里dpij的意思是说当第i个司机被分配完了订单以后， 订单的状态应该是j。 j里面bit里面的1表示的是这个订单被分配出去了。
# 
# 然后我们开始循环， 从把第0个司机分配每种订单开始作为初始状态。 然后从第一个司机开始， 所以这个时候， 应该就是有2个司机被分配完了， 我们用一个helper function去state里面， 把所有有2个1的给找出来， 其他的就丢掉。 然后开始转移， 转移的方法就是， 找到一个k， k表示要把第k个订单分给第i个司机， 那么转移方程就是， 当i-1个司机分配完， 状态里面是有i - 1个1， 并且这个状态prevstate跟j的唯一差别就是第k位上面的订单是要分给第i个司机的。 所有用个xor把第k位给搞成0， 就得到了prevstate， 然后我们当然要从这个所有的k里面找到最大的， 这个由两部分组成， 一个是对于前面i-1个司机， 还有个是第k个订单给第i个司机， 这2个要加起来最大才行。
# 
# 上面步骤做好以后， 那么最多多少分肯定能算出来。 然后我们就倒回去算到底怎么匹配的。 首先， 我们要知道最后一个司机当state是11111的时候， allocation里面存的就是这个司机分的单号。 然后知道这个以后， 我们就把这个单号从state里面去掉就得到了上一个单号， 以此类推就做完了。
# 
# 当然我做的时候， 是在给driver分配订单， 其实是做反了的， 更好的办法应该是给订单分配driver， 这样return的时候， 不需要向我这样再倒腾一次。

class Solution:
    """
    @param score: When the j-th driver gets the i-th order, we can get score[i][j] points.
    @return: return an array that means the array[i]-th driver gets the i-th order.
    """
    def orderAllocation(self, score):
        num_states = 1 << len(score)
        # dp[i][j] = Driver i is assigned to state j
        dp = [[0] * num_states for _ in range(len(score))]
        max_score = 0
        last_order = -1
        allocation = [[-1] * num_states for _ in range(len(score))]
        for i in range(len(score)):
            bit_index = 1 << i
            dp[0][bit_index] = score[i][0]
            allocation[0][bit_index] = i
        for i in range(2, len(score) + 1):
            for j in range(num_states + 1):
                if self.num_of_ones(j) != i:
                    continue
                for k in range(len(score)):
                    if j & (1 << k) == 0:
                        continue
                    prev_state = j ^ (1 << k)
                    if dp[i - 2][prev_state] + score[k][i - 1] > dp[i - 1][j]:
                        dp[i - 1][j] = dp[i - 2][prev_state] + score[k][i - 1]
                        allocation[i - 1][j] = k
        driver_to_order = [-1] * len(score)
        last_state = num_states - 1
        for i in range(len(score) - 1, -1, -1):
            driver_to_order[i] = allocation[i][last_state]
            last_state = (1 << driver_to_order[i]) ^ last_state

        order_to_driver = [-1] * len(score)
        for driver, order in enumerate(driver_to_order):
            order_to_driver[order] = driver

        return order_to_driver

    def num_of_ones(self, state):
        num_of_ones = 0
        while state > 0:
            state -= self.lowbit(state)
            num_of_ones += 1
        return num_of_ones

    def lowbit(self, state):
        return state & (-state)

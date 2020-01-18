#!/usr/bin/python -t

# two pointers
#由于给出了数组A内的元素范围，所以我们可以遍历所有的组合情况，并计算当前组合下的数量来得出最终结果。所有的组合可能可以分为以下三种情况：
#
#三个元素均相等： a1 == a2 == a3
#只有两个元素相等： a1 == a2 && a2 != a3
#三个元素均不相等： a1 < a2 < a3
#注意以上的a1, a2, a3均表示值，即与下标无关，所以为了防止重复计算对于第二种情况不考虑 a2 == a3 && a1 != a2 这种情况，因为是完全等价的。同样的，第三种情况对元素进行了排序，因为无论是哪三个不同的元素，都会有一个大小排序，此时我们将a1, a2, a3分别对应即可。
#
#接下来我们计算每种情况下的组合数量，对于第一种情况，假设值为 a1 的元素有 n 个，并且因为题目中有要求说一个合法的元组需要下标是递增的，那么此组合的数量即为 从 n 个元素中取出 3 个 的组合问题，因此这个组合问题的结果为 n * (n - 1) * (n - 2) / 6 (即C(3, n)，参考维基百科)。
#同理，假设值为 a1 的数量为 n1，值为 a2 的数量为 n2，值为 a3 的数量为 n3，那么对于第二种情况的数量为 (n1 * (n1 - 1) / 2) * n3，对于第三种情况的数量为 n1 * n2 * n3


import collections

class Solution:
    """
    @param A: the given integer array
    @param target: the given integer target
    @return: the number of tuples
    """
    def threeSumMulti(self, A, target):
        # Write your code here
        A.sort()
        n = len(A)
        if n < 3:
            return 0
            
        mod = 10**9+7
        
        ret = 0
        
        cnt = collections.Counter(A)
        
        for i in range(101):
            for j in range(i, 101):
                k = target -i -j
                if k > 100 or k < 0:
                    continue
                
                if i == j and j == k:
                    ret += cnt[i]*(cnt[i]-1)*(cnt[i]-2)//6
                if i == j and j != k:
                    ret += cnt[i]*(cnt[i]-1)//2*cnt[k]
                elif k > j:
                    ret += cnt[i]*cnt[j]*cnt[k]
                    
        return ret%mod
        

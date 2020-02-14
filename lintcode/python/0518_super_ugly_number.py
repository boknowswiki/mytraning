#!/usr/bin/python -t

# heap

# 做法1:
# 
# 使用小根堆, 初始将1放入堆, 循环 n-1 次, 每次取出堆顶, 然后将该值与素数列表每个数的乘积再次放入堆.
# 
# 注意可能会有数重复入堆, 所以还需要额外的数据结构记录一个数是否出现过, 把重复的数排除, 以保证取出的堆顶是从小到大的超级丑数.
# 
# n-1 次循环之后, 此时的堆顶即是第 n 个丑数.
# 
# 时间复杂度 O(nklogn)
# 
# 做法2:
# 
# 依次求出前n个超级丑数. 定义times[i]表示当前的超级丑数的质因数中, 列表中第i个素数的次数. uglys[i]表示第i+1个素数.
# 
# 初始 times[i] = 0, uglys[0] = 1, 然后依次由 uglys[0] ~ uglys[i] 求出 uglys[i+1]:
# 
# 枚举, 求出 uglys[times[j]] * prime[j] 的最小值, 即是 uglys[i+1]
# 更新对应的 times[j], 即 若 uglys[times[j]] * prime[j] == uglys[i+1], times[j]++
# 时间复杂度 O(nk)
# 
# 可参考 https://blog.csdn.net/happyaaaaaaaaaaa/article/details/50850473


import heapq

class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        # write your code here
        m = len(primes)
        times = [0] * m
        ugly = [1]
        heap = [(primes[i]*ugly[times[i]], i) for i in range(m)]
        heapq.heapify(heap)
        
        while len(ugly) < n:
            val, min_times = heapq.heappop(heap)
            times[min_times] += 1
            # make sure no same number
            if val != ugly[-1]:
                ugly.append(val)
                
            heapq.heappush(heap, (primes[min_times]*ugly[times[min_times]], min_times))
            
        #print ugly
            
        return ugly[-1]
        


#!/usr/bin/python -t

# sweep line and presum

"""
给定一个区间组成的数组A，每个区间代表一个会议的开始和结束时间。
一共有room个会议室。再给定若干个询问，问(a , b)这个会议是否可以加入。

思路是pre-calculation: 开一个数组M，对于会议(a, b)，我们让M[a]加1，然后让M[b]减1。A遍历完之后，M[x]代表的是x这个时刻有多少个会议同时在进行。
如果M[x] < rooms，那么说明这个时刻是可以插入新会议的，否则说明不能.
我们可以用一个数组P来标记每个时刻是否需要新会议室（也就是如果来了新会议，是否需要新的会议室），如果不需要，则标记为0，否则标记为1，
那么：P[x] = 0 if M[x] < rooms, else 1.
给定新的会议(a, b)问题就转化为，问[a, a+1, . . . , b−1]这些位置上的P是否都是0，
也就是问以P[a−1]为结尾的前缀和是否等于以P[b-1]结尾的前缀和。所以只需要再缓存一下P的前缀和就行了
"""
class Solution:
    def meetingRoomIII(self, intervals, rooms, queries):
        max_end = max(max(end for _, end in intervals), max(end for _, end in queries))

        # cnter[x]代表的是x这个时刻有多少个会议同时在进行，算法: 只记录上升沿和下降沿
        cnter = [0 for _ in range(max_end + 1)]
        for start, end in intervals:
            cnter[start] += 1   # 只记录上升沿和下降沿
            cnter[end] -= 1

        # need[x]表示x时刻是否需要新会议室（也就是如果来了新会议，是否需要新的会议室）
        need = [0 for _ in range(max_end + 1)]
        need_cnt = 0
        for i in range(max_end + 1):
            need_cnt += cnter[i]
            if need_cnt >= rooms:
                need[i] = 1

        # 构造前缀和presums
        presums = [0 for _ in range(max_end + 2)]
        for i in range(max_end + 1):
            presums[i+1] = presums[i] + need[i]

        # 给定新的会议(a, b)问题就转化为，问[a, a+1, . . . , b−1]这些位置上的need是否都是0
        res = []
        for start, end in queries:
            if presums[end] == presums[start]:   # [a, a+1, . . . , b−1]这些位置上的need是否都是0
                res.append(True)
            else:
                res.append(False)
        return res



# 扫描线+前缀和精华版
# 这道题之所以被称为精华版， 是因为这个题目把2种算法用到了极致。
# 
# 首先， 开一个范围那么大的数组， 然后对于每个interval， mark一下不available。 也就是用了+1没用-1.
# 
# 然后， 其实可以另外开一个数组， 等等再常数级别优化， 这个时候， 我们有了整个所有time的占用情况， 这个时候知道每个时间， 占用了几个。
# 
# 然后我们根据占用情况， 反推出可用情况， 就是占用跟总房间去比。
# 
# 然后妙的来啦， 怎么样在常数时间， 知道每个ask行不行呢？这里我们直接把available的时间标成1， 不available标成0. 然后再去算一个前缀和。 然后看一下前缀和和出来， 和区间长度比较， 如果区间里面都是1，那么加起来肯定等于区间长度。 那么这个题目答案就出来了

class Solution:
    """
    @param intervals: the intervals
    @param rooms: the sum of rooms
    @param ask: the ask
    @return: true or false of each meeting
    """
    def meetingRoomIII(self, intervals, rooms, asks):
        time = [0] * 500001
        for interval in intervals:
            time[interval[0]] += 1
            time[interval[1]] -= 1

        last = time[0]
        available = [0] * 500001
        available[0] = 1 if last < rooms else 0
        for i in range(1, len(available)):
            curr = last + time[i]
            if curr < rooms:
                available[i] = available[i - 1] + 1
            else:
                available[i] = available[i - 1]
            last = curr

        results = []
        for ask in asks:
            result = available[ask[1] - 1] - available[ask[0] - 1] >= ask[1] - ask[0]
            results.append(result)
        return results

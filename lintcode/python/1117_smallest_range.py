#!/usr/bin/python -t

# heap

import heapq

class Solution:
    """
    @param nums: k lists of sorted integers
    @return: the smallest range that includes at least one number from each of the k lists
    """
    def smallestRange(self, nums):
        # write your code here
        q = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapq.heapify(q)
        low, high = q[0][0], max(q[i][0] for i in range(len(nums)))
        large = high
        while True:
            _, row, col = q[0]
            if col+1 == len(nums[row]):
                break
            next = nums[row][col+1]
            heapq.heappushpop(q, (next, row, col+1))

            small, large = q[0][0], max(large, next)
            if large-small < high-low:
                low, high = small, large

        return low, high



# two pointers

#考点：
#
#双指针区间维护
#题解：
#
#首先由于各个序列升序排列，开始利用current数组，筛选出所有序列的最小值中最大的数字，因为最终答案的右边界肯定大于等于该值，所以从该值开始。
#然后在for循环内对所有序列遍历，使得每个current[i]保存了每个序列中最接近maxValue并且小于maxValue的数字下标，同时选出每个序列中最接近maxValue并且小于maxValue的数字最小值。
#得到左右边界后，判断是否更新答案。
#如果当前current[i]指向的不是该序列的最后一个数字，则current[i]++，即右移，将对应数字设为右边界，将之前的最小值从维护的区间去除，重新维护。
#如果指向为最后一个则无法移动，返回结果即可。


class Solution:
    """
    @param nums: k lists of sorted integers
    @return: the smallest range that includes at least one number from each of the k lists
    """
    def smallestRange(self, nums):
        current=[0 for i in range(len(nums))]
        res=[0,0]
        result=sys.maxsize
        maxvalue=-sys.maxsize
        maxindex=0
        flag=1
        #确定刚开始的右边界
        for i in range(0,len(nums)):
            #每一个都是升序排列
            if nums[i][current[i]]>maxvalue:
                maxindex=i #最大值在第几个
                maxvalue=nums[i][current[i]]
        while flag:
            minindex,minvalue=0,sys.maxsize
            #确定左边界
            for i in range(len(nums)):
                #current[i]表示的是保存了每个序列中最接近maxvalue并且小于maxvalue的数字下标。
                #判断第几个数是<=maxvalue的,直到大于maxvalue的值以后停止累加
                while current[i]+1<len(nums[i]) and nums[i][current[i]+1]<=maxvalue:
                    current[i]+=1
                #current[i]表示当前第i个序列中的下标为current[i]的数是最接近maxvalue的，然后比较每个序列的大小
                if nums[i][current[i]]<minvalue:
                    minindex=i
                    minvalue=nums[i][current[i]]
            #判断是否更新
            if maxvalue-minvalue<result:
                result=maxvalue-minvalue
                res[0]=minvalue
                res[1]=maxvalue
            if current[minindex]==len(nums[minindex])-1:
                flag=0
            else:
                current[minindex]+=1 #往后移，将这个值作为最大值
                maxindex=minindex #指向第几个
                maxvalue=nums[maxindex][current[minindex]]
        return res

if __name__ == '__main__':
    s = Solution()
    a = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    print(s.smallestRange(a))

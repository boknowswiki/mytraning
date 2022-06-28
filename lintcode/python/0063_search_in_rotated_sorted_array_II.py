#!/usr/bin/python3 -t

# 解题思路
# 旋转数组的部分相关题目整理如下：
# | ** 题目 ** | ** 有重复元素 ** | ** 目标任务 ** |
# |:----|:----:|:----|:----:|:----|:----:|
# | 159. 寻找旋转排序数组中的最小值 | × | 寻找最小值 |
# | 160. 寻找旋转排序数组中的最小值 II | √ | 寻找最小值 |
# | 62. 搜索旋转排序数组 | × | 寻找target |
# | 63. 搜索旋转排序数组 II | √ | 寻找target |
#
# 这道题是T62的延伸问题，区别在于数组中可以有重复元素。
#
# 我们采用的方法是借助T160的方法寻找数组中的中枢点pivot，然后通过中枢点把数组分为有序的两个子数组，最后在target所在的子数组中进行二分查找。平均时间复杂度为O(log(n))O(log(n))，最差的时间复杂度为O(n)O(n)。
#
# 算法流程
# step1：二分搜索找中枢点
# 中枢点是旋转数组最大值和最小值的分界点，对应到数组在旋转之前是第0位元素。
#
# 具体做法，设置双指针left和right，初始化指向数组A两端。
#
# 第一次分类讨论：比较A[left]和A[right]
#
# 如果A[left] < A[right]，说明数组没有旋转过，仍然是升序排列。我们直接return A[left]。
#
# 反之，说明数组非单调，进入到第二次分类讨论。
#
# 第二次分类讨论：比较A[mid]和A[right]，其中mid是二分中点。
#
# 如果A[mid] < A[right]，可以证明此时数组右半边是升序的（严格来说是非降序的），那我们就不用考虑右半边了。中枢点一定在[left, mid]间，令right = mid。
#
# 如果A[mid] > A[right]，可以证明此时数组左半边是升序的（同理，应为非降序），于是我们不需要考虑左半边。中枢点一定在(mid, right]间，令left = mid + 1。
#
# 如果A[mid] == A[right]，再讨论
#
# 如果right前的元素比right大，那么right就是中枢点
#
# 否则，right左移
#
# 直到left == right时，此时left指向的就是中枢点pivot。
#
# step2：以中枢点为界分成两个有序子数组
# 利用中枢点把数组分成两个有序数组，通过比较target和A[0]的大小关系，确定target在哪段数组。
#
# 如果target >= A[0]，target在[0, pivot - 1]之间。
#
# 反之，target在[pivot, len(A) - 1]之间。
#
# 当然，这里的特殊情况是pivot == 0，即数组本身就是有序的，此时target有可能在全数组的任意位置。
#
# step3：对子数组进行二分查找
# 走到这一步，该问题已经转化为如何在有序数组中寻找目标元素，是典型的二分查找问题。直接借用二分查找的模板即可。
class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        if not len(A):
            return False
        # step1: find pivot
        left, right = 0, len(A)-1
        while(left < right):
            mid = left + (right-left)//2
            if A[mid] > A[right]:
                left = mid + 1
            elif A[mid] < A[right]:
                right = mid
            else:
                if (right > 0 and A[right - 1] > A[right]):
                    left = right
                else:
                    right -= 1
        pivot = left
        # step2: split
        if pivot == 0:
            left, right = 0, len(A)-1
        elif target >= A[0]:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, len(A) - 1
        # step3: find target
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid
        if A[left] == target:
            return True
        if A[right] == target:
            return True
        return False


# binary search
# time O(logn), worst case O(1)
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, a: List[int], target: int) -> bool:
        # write your code here
        n = len(a)
        if n == 0:
            return False
        if n == 1:
            return True if a[0] == target else False

        start = 0
        end = n - 1
        while start + 1 < end:
            if a[start] == target:
                return True
            if a[end] == target:
                return True

            mid = start + (end-start)//2
            if a[mid] == target:
                return True
            if a[start] <= a[mid]:
                if a[start] == a[mid]:
                    start += 1
                    continue
                if a[start] <= target <= a[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if a[mid] <= target <= a[end]:
                    start = mid
                else:
                    end = mid

        if a[start] == target:
            return True
        if a[end] == target:
            return True
        return False



if __name__ == '__main__':
    s = Solution()
    a = [4, 5, 1, 2, 3]
    b = 1
    a = [0,1,2,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
    b = -9
    a = [1001, 10001, 10007, 1, 10, 101, 201]
    b= 10001
    a = [3,4,4,5,7,0,1,2]
    b = 4
    a = [9,5,6,7,8,9,9,9,9,9,9]
    b = 8

    print(s.search(a, b))

# binary search solution

class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here
        n = len(A)
        if n == 0:
            return False
        
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            if A[mid] == target:
                return True
                
            if A[mid] > A[l]:
                if A[l] <= target < A[mid]:
                    r = mid
                else:
                    l = mid+1
            elif A[mid] < A[l]:
                if A[mid] < target <= A[r]:
                    l = mid+1
                else:
                    r = mid
            else:
                l += 1
                    
        print l
        if A[l] == target:
            return True
        else:
            return False

if __name__ == '__main__':
    s = [9,5,6,7,8,9,9,9,9,9,9]
    t = 8
    ss = Solution()
    print "answer is\n"
    print ss.search(s, t)

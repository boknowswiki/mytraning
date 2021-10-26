#!/usr/bin/python -t

# 正确的算法请参考: http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf

# time O(m+n)

class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        m, n = len(A), len(A[0])
        return self.find(A, 0, m-1, 0, n-1)
        
    def find(self, A, top, bottom, left, right):
        row_mid = (top+bottom)/2
        col_mid = (left+right)/2
        max_num = A[row_mid][col_mid]
        row, col = row_mid, col_mid
        
        # find max_num in row
        for i in range(top, bottom+1):
            if A[i][col_mid] > max_num:
                max_num = A[i][col_mid]
                row = i
                col = col_mid
                
        # find max_num in col
        for j in range(left, right+1):
            if A[row_mid][j] > max_num:
                max_num = A[row_mid][j]
                col = j
                row = row_mid
                
        if row -1 >= 0 and A[row-1][col] > A[row][col]:
            row -= 1
        elif row+1 < len(A) and A[row+1][col] > A[row][col]:
            row += 1
        elif col - 1 >= 0 and A[row][col-1] > A[row][col]:
            col -= 1
        elif col + 1 < len(A[0]) and A[row][col+1] > A[row][col]:
            col += 1
        else:
            return [row, col]

        
        if (row >= top and row < row_mid and col >= left and col < col_mid):
            return self.find(A, top, row_mid - 1, left, col_mid - 1)
        elif (row >= top and row < row_mid and col >= col_mid and col <= right):
            return self.find(A, top, row_mid - 1, col_mid + 1, right)
        elif (row > row_mid and row <= bottom and col >= left and col < col_mid):
            return self.find(A, row_mid + 1, bottom, left, col_mid - 1)
        elif (row > row_mid and row <= bottom and col > col_mid and col <= right):
            return self.find(A, row_mid + 1, bottom, col_mid + 1, right)
        
        return [-1, -1]


# O(mLogN)。这道题的面试标准答案。面试时，你能写出这样，就是Hire，follow-up问题能答好，就是Strong Hire。
# 
# 要点是：
# 
# 不要用系统max函数，因为你即需要最值也需要最值下标。
# 要lo<=hi，不要lo+1<hi。下标移动要快，lo+1<hi有维和感。
# follow-up，当然可以说，m > n 时，可以写成 O(nLogM)
# 
# 追求那个O(m+n)的解法，对于准备面试是纯粹浪费时间。Erik Demaine是14岁大学毕业的神童，20岁当上麻省理工的教授，他是第一个在课堂上讲这个
# O(m+n)解的。Erik自己要是没想过这题，面试30分钟，也不一定能写完O(m+n)解。难道面试官指望招得到比Erik Demaine还聪明的人？

class Solution:
    """
    @param A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        m = len(A)
        n = len(A[0])
        l = 1
        r = n-2
        while l <= r:
            mid = (l+r)//2
            colMax, row = A[0][mid], 0
            for i in range(1, m-1):
                if A[i][mid] > colMax:
                    colMax = A[i][mid]
                    row = i

            if A[row][mid] < A[row][mid-1]:
                r = mid-1
            elif A[row][mid] < A[row][mid+1]:
                l = mid+1
            else:
                # print("num is ", A[row][mid])
                return (row, mid)

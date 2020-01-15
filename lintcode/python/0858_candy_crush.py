#!/usr/bin/python -t

# two pointers
#这道题目可能比较难写, 但是思路是很简单的: 只要局面不稳定, 那就消除, 下落.
#
#代码的大题框架就是: 搜寻可以消除的块, 如果没有则局面稳定, 反之消除, 下落, 继续搜寻.
#
#不过需要注意几个细节:
#
#L型或者是十字型的可消除块要求的是行/列都需要至少3个相同的糖果
#下落之后上方的空位补零
#你不能只找到一个可以消除的块就立即消除然后下落, 而是找到当前局面中所有可以消除的块, 一次性消除, 然后下落, 这样才到达下一个局面, 再次判断.
#
#我们可以这样实现: 因为给定的类型都是正数, 所以我们可以在一次搜寻中, 把所有可消除的块都转换成负数.
#
#这样, 遍历整个地图完成一次搜寻后, 负数的块代表的就是可消除的, 置为0然后处理下落即可.

class Solution:
    """
    @param board: a 2D integer array
    @return: the current board
    """
    def candyCrush(self, board):
        # Write your code here
        m = len(board)
        n = len(board[0])
        found = True
        
        while found:
            found = False
            for i in range(m):
                for j in range(n):
                    val = abs(board[i][j])
                    if val == 0:
                        continue
                    if j < n-2 and abs(board[i][j+1]) == val and abs(board[i][j+2]) == val:
                        found = True
                        index = j
                        while index < n and abs(board[i][index]) == val:
                            board[i][index] = -val
                            index += 1
                            
                    if i < m-2 and abs(board[i+1][j]) == val and abs(board[i+2][j]) == val:
                        found = True
                        index = i
                        while index < m and abs(board[index][j]) == val:
                            board[index][j] = -val
                            index += 1
                            
            if found:
                for j in range(n):
                    index = m-1
                    for i in range(m-1, -1, -1):
                        if board[i][j] > 0:
                            board[index][j] = board[i][j]
                            index -= 1
                    for k in range(index, -1, -1):
                        board[k][j] = 0
                        
        return board
        

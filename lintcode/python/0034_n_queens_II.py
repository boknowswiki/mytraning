#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        if not n:
            return 0
            
        self.sum = set()
        self.diff = set()
        self.col = set()
        self.ret = 0

        self.dfs(0, n)
        
        return self.ret
        
    def dfs(self, row, n):
        if row == n:
            self.ret += 1
            return
        
        for i in range(n):
            if i not in self.col and (row+i) not in self.sum and (row-i) not in self.diff:
                self.col.add(i)
                self.sum.add(row+i)
                self.diff.add(row-i)
                self.dfs(row+1, n)
                self.col.remove(i)
                self.sum.remove(row+i)
                self.diff.remove(row-i)
                
        return
    
        
        
if __name__ == '__main__':
    s= 2
    ss = Solution()
    print "answer is %s" % ss.totalNQueens(s)


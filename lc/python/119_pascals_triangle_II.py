#!/usr/bin/python -t


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


#Time O(n2) space O(k)

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = [1]* (rowIndex+1)
        
        for i in range(rowIndex+1):
            for j in range(i-1, 0, -1):
                l[j] = l[j-1] + l[j]
                
        return l

if __name__ =='__main__':
    s = Solution()
    print s.getRow(3)

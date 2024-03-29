#!/usr/bin/python -t

# array
# time O(n^2)
# space O(n)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for row in range(rowIndex+1):
            level = [0] * (row+1)
            level[0] =level[-1] = 1

            for i in range(1, row):
                level[i] = prev[i-1] + prev[i]

            prev = level

        return level

#Time O(n), space O(k)
#from jiuzhang

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r = []
        val = 1
        r.append(val)
        
        for i in range(rowIndex, 0, -1):
            val = val * i
            val = val / (rowIndex -i + 1)
            r.append(val)
            
        #r.append(1)
        
        return r


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

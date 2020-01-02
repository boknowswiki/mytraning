#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        d = {}
        
        for i, num in enumerate(numbers):
            if target - num in d:
                return [d[target-num], i]
            else:
                d[num] = i
                
        return [-1, -1]

        
        
if __name__ == '__main__':
    s = [2,7,11,15]
    t = 9

    ss = Solution()
    print "answer is %s" % ss.twoSum(s, t)


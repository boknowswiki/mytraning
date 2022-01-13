#!/usr/bin/python -t


#在leetcode的讲解中看到了一个很好的位运算办法，而且也很简单易懂，思路也很简单。
#index: 0123
#value: 0134
#missing
#=4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
#=(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
#=0∧0∧0∧0∧2
#=2
#如果不缺数，再加上最大数应该对应的索引（也就是所给的数里面缺的索引，比如上面的例子，没有4号索引），每个数以及它应该对应的索引取
#异或，整体再去异或，应该为0，但是由于缺少了一个数，所以整体异或之后所得的结果就是那个缺少的数。

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        missing = len(nums)
        for i, n in enumerate(nums):
            missing ^= i ^ n
        return missing


class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        n = len(nums)
        total = (1+n)*(n)//2
        for num in nums:
            total -= num

        return total

        
if __name__ == '__main__':
    s = Solution()
    a = [0,1,3]
    a = [1,2,3]
    print(s.findMissing(a))
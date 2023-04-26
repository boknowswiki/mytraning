# math

# time O(1)
# space O(1)
# solution: https://leetcode.com/problems/add-digits/editorial/

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
      
      
# time O(n)
# space O(1)

class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            total = 0
            while num >= 1:
                if num >= 10:
                    total += num//10
                    num = num % 10
                else:
                    total += num
                    break

            num = total

        return num

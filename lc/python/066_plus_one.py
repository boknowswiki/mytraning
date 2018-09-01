#!/usr/bin/python -t

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        c = 1
        for i in xrange(n-1, -1, -1):
            print digits[i]
            print c
            if digits[i] < 9:
                digits[i] = digits[i] + c
                return digits
            else:
                digits[i] = 0
                c = 1

        if c == 1:
            digits.insert(0, c)

        return digits


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = 1
        while carry:
            if i > len(digits):
                digits.insert(0, 1)
                carry = 0
            else:
                num = digits[len(digits) - i]
                digits[len(digits) - i] = (num + 1) % 10
                carry = (num + 1) // 10
                i += 1
        return digits

if __name__ =='__main__':
    s = Solution()
    print('%s\n' % (s.plusOne([8,9,9,9])))


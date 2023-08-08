#!/usr/bin/python -t

# array
# time O(n)
# space O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 0:
            return [1]

        def reverse(arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

            return arr

        nums = reverse(digits)
        ret = []
        c = 1
        index = 0

        while index < n or c:
            val = nums[index] if index < n else 0
            val += c
            ret.append(val%10)
            c = val//10

            index += 1

        return reverse(ret)

#best solution

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        
        while digits[n] == 9:
            digits[n] = 0
            n = n - 1
            
        if n < 0:
            digits.insert(0, 1)
        else:
            digits[n] = digits[n] + 1
            
        return digits

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        ret = [0] * n
        c = 0

        for i in range(n-1, -1, -1):
            if i == n-1:
                ret[i] = (digits[i] + 1) %10
                c = (digits[i]+1) / 10
                continue
                
            ret[i] = (digits[i] + c) % 10
            c = (digits[i]+c)/10
            
        if c == 1:
            ret.insert(0,1)
            
        return ret

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


#!/usr/bin/python -t

# time O(logn)
# space O(logn)

class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        # Base case, to stop recursive calls.
        if n == 0:
            return 1
       
        # Handle case where, n < 0.
        if n < 0:
            return 1.0 / self.binaryExp(x, -1 * n)
       
        # Perform Binary Exponentiation.
        # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
        else:
            return self.binaryExp(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)


# math
# time O(n)
# space O(1)


# time limitaion exceeded with following case:
# x = 0.00001, n = 2147483647

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        multiple = True
        if n == 0:
            return 1
        if n > 0:
            multiple = True
        else:
            multiple = False

        #print(f"multiple {multiple}")
        n = abs(n)

        for i in range(n):
            if multiple:
                ret *= x
            else:
                ret /= x

            #print(f"ret {ret}")

        return ret

#time O(logn) space O(logn)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x

        if n < 0:
            x = 1/x
            n = -n
        
        i = n/2
        mod = n%2
        
        val = self.myPow(x*x, i)
        
        if mod != 0:
            val = val * self.myPow(x, mod)

        return val

class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


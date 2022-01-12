#!/usr/bin/python -t

class Solution:
    """
    @param k: The k
    @param a: The A
    @param b: The B
    @return: The answer
    """
    def addition(self, k, a, b):

        for i in range(len(a)):
            if a[i] == '0':
                continue
            a_nozero = a[i:]
            break
        for i in range(len(b)):
            if b[i] == '0':
                continue
            b_nozero = b[i:]
            break


        i = len(a_nozero) - 1
        j = len(b_nozero) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0:
            digit_a = (ord(a_nozero[i]) - ord('0')) if i >= 0 else 0
            digit_b = (ord(b_nozero[j]) - ord('0')) if j >= 0 else 0
            val = (digit_a + digit_b + carry) % k
            carry = (digit_a + digit_b + carry) // k
            result.append(val)
            i -= 1
            j -= 1

        if carry > 0:
            result.append(carry)

        return ''.join([str(i) for i in result[::-1]])

#!/usr/bin/python -t

class Solution:
    """
    @param N: That means you should return the N-th magical number.
    @param A: Parameter A.
    @param B: Parameter B.
    @return: Return the N-th magical number. 
    """
    def nthMagicalNumber(self, N, A, B):
        # Write your code here.
        MOD = 10**9 + 7

        L = A / self.gcd(A, B) * B
        M = L / A + L / B - 1
        #print L, A, B, M
        q, r = divmod(N, M)

        if r == 0:
            return q * L % MOD

        heads = [A, B]
        for _ in xrange(r - 1):
            if heads[0] <= heads[1]:
                heads[0] += A
            else:
                heads[1] += B

        return (q * L + min(heads)) % MOD
        
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)

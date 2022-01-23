#!/usr/bin/python3 -t

class Solution:
    """
    @param S: The given string S
    @param T: The given string T
    @return: any permutation of T (as a string) that satisfies this property
    """
    def customSortString(self, S, T):
        # Write your code here
        ret = ""
        cnt = [0] * 26

        for i in range(len(T)):
            cnt[ord(T[i])-ord('a')] += 1

        for i in range(len(S)):
            for j in range(cnt[ord(S[i])-ord('a')]):
                ret += S[i]
            cnt[ord(S[i])- ord('a')] = 0

        for i in range(26):
            for j in range(cnt[i]):
                ret += chr(ord('a')+i)

        return ret
        
if __name__ == '__main__':
    s = Solution()
    a = "cba"
    b = "abcd"
    print(s.customSortString(a,b))
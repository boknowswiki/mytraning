#!/usr/bin/python -t

# hash table


import collections

class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        return sum(v % 2 for v in collections.Counter(s).values()) < 2



import collections

class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        odd_cnt = 0
        for v in collections.Counter(s).values():
            if v % 2:
                if odd_cnt == 1:
                    return False
                else:
                    odd_cnt += 1
                    
        return True
        

#!/usr/bin/python -t

class Solution:
    """
    @param words: the array of string means the list of words
    @param order: a string indicate the order of letters
    @return: return true or false
    """
    def isAlienSorted(self, words, order):
        # write your code here.
        d = {}
        for i in range(len(order)):
            d[order[i]] = i

        for i in range(1, len(words)):
            if not self.is_valid(d, words[i-1], words[i]):
                return False

        return True

    def is_valid(self, d, a, b):
        for i in range(min(len(a), len(b))):
            if d[a[i]] < d[b[i]]:
                return True
            elif d[a[i]] > d[b[i]]:
                return False

        return len(a) <= len(b)

        
if __name__ == '__main__':
    s = Solution()
    a = ["hello","leetcode"]
    b = "hlabcdefgijkmnopqrstuvwxyz"

    print(s.isAlienSorted(a, b))
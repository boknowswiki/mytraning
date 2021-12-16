#!/usr/bin/python -t

# hash table and string

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        d = {}
        for i in range(len(str)):
            if str[i] not in d:
                d[str[i]] = [0, i]
            d[str[i]][0] += 1

        minIndex = len(str)-1
        ret = ""
        for k in d:
            if d[k][0] == 1 and (d[k][1] < minIndex or ret == ""):
                minIndex = d[k][1]
                ret = k

        return ret

if __name__ == '__main__':
    s = Solution()
    a = "abaccdeff"
    a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    print(s.firstUniqChar(a))
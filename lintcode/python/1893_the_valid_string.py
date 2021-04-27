#!/usr/bin/python -t

class Solution:
    """
    @param s: a string
    @return: if valid return "YES" else return "NO"
    """
    def isValid(self, s):
        # write your code here
        hash = [0]*26
        for i in s:
            hash[ord(i)-97] += 1

        first = second = 0
        sum_first = sum_second = 0
        print(hash)
        for i in hash:
            
            if i > 0:
                print("i is %d, first %d, second %d" % (i, first, second))
                if first == 0:
                    first = i
                    sum_first = 1
                elif i == first:
                    sum_first += 1
                elif second == 0:
                    second = i
                    sum_second = 1
                elif i == second:
                    sum_second += 1
                else:
                    return "NO"
        if (second == 0) or ((first == 1 or first == second + 1) and sum_first == 1) or ((second == 1 or second == first + 1) and sum_second == 1):
            return "YES"
        return "NO"

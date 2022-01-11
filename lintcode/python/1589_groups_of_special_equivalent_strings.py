#!/usr/bin/python -t

# string

class Solution:
    """
    @param A: a string array
    @return: Return the number of groups of special-equivalent strings from A.
    """
    def numSpecialEquivGroups(self, A):
        # write your code here
        s = set()
        for word in A:
            tup = [0]*52
            for i in range(len(word)):
                tup[(ord(word[i])-ord('a')) + 26*(i %2)] += 1 
                print(tup)
            s.add(tuple(tup))
        return len(s)

        
if __name__ == '__main__':
    s = Solution()
    a = ["a","b","c","a","c","c"]

    print(s.numSpecialEquivGroups(a))
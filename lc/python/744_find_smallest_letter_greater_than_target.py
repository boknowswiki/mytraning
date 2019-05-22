#!/usr/bin/python -t

#time O(logn) space O(1)

'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        l = 0
        r = n - 1
        
        while l < r:
            m = l + (r-l)/2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m
                
        return letters[0] if letters[l] <= target else letters[l]
'''

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        l = 0
        i = n-1
        
        while i > 0:
            s = i/2
            need = l + s
            if need < n and letters[need] <= target:
                l = need+1
                i = i - s +1
            else:
                i = s

        return letters[0] if l == n else letters[l]

if __name__ =='__main__':
    s = ['c', 'f', 'j']
    ss = Solution()
    print('answer is %s' % ss.nextGreatestLetter(s, 'j'))

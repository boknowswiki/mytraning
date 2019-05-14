#!/usr/bin/python -t

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n_s = len(s)
        n_t = len(t)
        
        if n_s != n_t:
            return False
        
        ss = sorted(s)
        tt = sorted(t)
        
        if cmp(ss, tt) == 0:
            return True
        else:
            return False

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d={}
        
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
                
                
        for i in t:
            if i in d:
                d[i] = d[i] - 1
            else:
                return False
            
        for key in d:
            if d[key] != 0:
                return False
            
        return True

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def insert_sort(s):
            s = list(s)
            n = len(s)
            if n == 0:
                return []
            
            for i in range(1, n):
                j = i
                while j > 0 and s[j-1] > s[j]:
                    s[j-1], s[j] = s[j], s[j-1]
                    j = j - 1
                    
            return s
        
        n_s = insert_sort(s)
        n_t = insert_sort(t)
        for i in n_s:
            print i

        for j in n_t:
            print j
        print 'done'
        #for i, j in n_s, n_t:
        #    if i != j:
        #        return False
            
        return True

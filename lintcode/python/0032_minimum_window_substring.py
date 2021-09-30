#!/usr/bin/python -t

# two pointers
#同向双指针的万能套路就是for 循环右指针，然后移动左指针until invalid
#双指针滑动窗口算法，简易高效:
#1.滑动窗口右端,直达满足最小覆盖子串
#2.滑动窗口左端以对窗口长度进行优化,左移至打破子串全覆盖的前一个字符
#3.更新最小值
#4.循环前3个步骤



class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        n = len(source)

        d = {}
        for t in target:
            d[t] = d.get(t, 0) + 1

        ret = float("inf")
        start, end = -1, -1
        needed = len(d)
        #print("start need", needed)
        left = 0


        #print(d)
        for right in range(n):
            c = source[right]
            #print(c)
            if c in d:
                #print("reduce", c, d)
                d[c] -= 1
                if d[c] == 0:
                    needed -= 1
                    #print("needed", needed)
            
            while needed == 0 and left <= right:
                #print(left, right)
                if right - left+1 < ret:
                    ret = right-left+1
                    start, end = left, right
                    #print ("update", start, end)
                l_c = source[left]
                if l_c in d:
                    if d[l_c] == 0:
                        needed += 1
                    d[l_c] += 1
                left += 1

        return source[start:end+1] if start != -1 else ""
                    

class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        n = len(source)
            
        d = {}
        
        for c in target:
            d[c] = d.get(c, 0) + 1
            
        needed = len(d)
        left = 0
        ret, start, end = sys.maxint, -1, -1
        
        for right in range(n):
            c = source[right]
            if c in d:
                d[c] -= 1
                if d[c] == 0:
                    needed -= 1
            
            while needed == 0:
                if right-left + 1 < ret:
                    ret = right-left+1
                    start, end = left, right
                ch = source[left]
                if ch in d:
                    if d[ch] == 0:
                        needed += 1
                    d[ch] += 1
                    
                left += 1
                
        return source[start:end+1] if start != -1 else ''
        
        

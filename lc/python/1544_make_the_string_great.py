
# string and two pointer
# time O(n)
# space O(1) in c or c++, in python it's O(n)

class Solution:
    def makeGood(self, s: str) -> str:
        s_list = list(s)
        
        end = 0
        
        for start in range(len(s_list)):
            if end > 0 and abs(ord(s_list[start]) - ord(s_list[end-1])) == 32:
                end -= 1
            else:
                s_list[end] = s_list[start]
                end += 1
                
        return "".join(s_list[:end])
      
# string and stack
# time O(n)
# space O(n)

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        n = len(s)
        if n == 0 or n == 1:
            return s
        
        for c in list(s):
            if stack and abs(ord(c)-ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
                
        return "".join(stack)

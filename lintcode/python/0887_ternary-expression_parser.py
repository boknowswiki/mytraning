#!/usr/bin/python -t

# stack
#用栈从后往前，遇到数字放进栈里。
#遇到T就保留栈顶的，删掉第二个。
#遇到F就删除栈顶的，保留第二个。

class Solution:
    """
    @param expression: a string, denote the ternary expression
    @return: a string
    """
    def parseTernary(self, expression):
        # write your code here
        i = len(expression) - 1
        s = []
        
        while i > 0:
            if expression[i] == '?':
                left, right = s.pop(-1), s.pop(-1)
                s.append(left if expression[i-1] == 'T' else right)
                i -= 1
            elif expression[i] != ':':
                s.append(expression[i])
                
            i -= 1
            
        return s[0]
        
        
        

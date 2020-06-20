#!/usr/bin/python -t

# using stack
# time O(n)


class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return ""
            
        stack = []
        
        for c in s:
            if c != "]":
                stack.append(c)
                continue
            
            substrings = []
            
            while len(stack) != 0 and stack[-1] != "[":
                substrings.append(stack.pop())
                
            # skip "["
            stack.pop()
            
            repeats = 0
            base = 1
            
            while len(stack) != 0 and stack[-1].isdigit():
                repeats += (ord(stack.pop()) - ord('0')) * base
                base *= 10
                
            stack.append(''.join(reversed(substrings)) * repeats)
            
        return ''.join(stack)

# recursion
# 递归版本 四种情况 1）是数字，就累加之前有的数字 2）是左括号，从左括号之后开始递归。递归要传回两个值：组成的substring，递归结束的位置。 之后把传回的substring × 数字 加到结果里。数字归零。 3）是右括号，返回结果 4）是普通字母，直接加到结果里 感觉这种思路比较简洁好懂一些

class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return s
            
        ret, _ = self.helper(s, 0)
        
        return ret
        
    
    def helper(self, s, pos):
        ret = ""
        repeats = 0
        
        while pos < len(s):
            if s[pos].isdigit():
                repeats = repeats*10 + int(s[pos])
            elif s[pos] == "[":
                substrings, pos = self.helper(s, pos+1)
                ret += substrings * repeats
                repeats = 0
            elif s[pos] == "]":
                return ret, pos
            else:
                ret += s[pos]
            pos += 1
            
        return ret, pos

